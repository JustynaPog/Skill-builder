#!/bin/python3
import boto3 
import argparse  


def get_user_input():
    """
    Collects user input from the command line for AWS region, port, and instance state.
    """
    parser = argparse.ArgumentParser()  
    parser.add_argument('region', type=str, help='Enter the AWS region')  
    parser.add_argument('port', type=int, help='Enter the port to check')
    parser.add_argument('state', type=int, choices=[0, 1], help='Enter instance status (1 for running, 0 for running and stopped)') 

    args = parser.parse_args() 
    return args.region, args.port, args.state  

def main():
    region, port, state = get_user_input()

    instance_states = ['running'] if state == 1 else ['running', 'stopped']

    ec2_client = boto3.client('ec2', region_name=region)

    try:
        sg_ids_with_open_port = []  # List to store Security Group IDs that have the specified port open

        # Retrieve all security groups in the specified region
        sg_response = ec2_client.describe_security_groups()

        # Iterate over each security group to check open ports
        for sg in sg_response['SecurityGroups']:
            sg_id = sg['GroupId'] 

            # Iterate over security group permissions (inbound rules)
            for permission in sg.get('IpPermissions', []):
                # Check if the specified port is open in both FromPort and ToPort
                if (
                    permission.get('FromPort') == int(port) and
                    permission.get('ToPort') == int(port)
                ):
                    sg_ids_with_open_port.append(sg_id)  # Add SG ID with the open port

        # Retrieve EC2 instances filtered by their state (running or running/stopped)
        instance_response = ec2_client.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': instance_states}] 
        )

        instance_to_sg = {}  # Dictionary to map instance IDs to their attached security groups

        # Iterate over all EC2 reservations and instances
        for reservation in instance_response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']  # Instance ID
                sg_ids = []  # List to store the security group IDs attached to the instance

                # Collect security groups attached to the instance
                for sg in instance['SecurityGroups']:
                    sg_ids.append(sg['GroupId'])

                # Map the instance ID to its security groups
                instance_to_sg[instance_id] = sg_ids

        # Initialize a new dictionary to store instances with security groups that have the open port
        filtered_instance_to_sg = {}

        # Iterate through the instance-to-security group mapping
        for instance_id, sg_ids in instance_to_sg.items():
            # Check if any attached security group has the open port
            for sg_id in sg_ids:
                if sg_id in sg_ids_with_open_port:
                    filtered_instance_to_sg[instance_id] = sg_ids  # Add to filtered results

                    # Convert security group IDs to a comma-separated string for display
                    sg_ids_str = ", ".join(sg_ids)

                    print(f"Instance Id: {instance_id}, Security Groups: {sg_ids_str}")

    except Exception as e:
        print(f"Error fetching security groups: {e}")


if __name__ == "__main__":
    main()
