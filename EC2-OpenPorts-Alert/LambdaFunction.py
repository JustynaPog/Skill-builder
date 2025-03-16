import boto3
import os
import json

# AWS Clients
ec2_client = boto3.client("ec2")
ses_client = boto3.client("ses")

SES_SENDER_EMAIL = os.getenv("SES_SENDER_EMAIL", "noreply@example.com")

# Default ports if the `OpenPorts` tag is not set
DEFAULT_PORTS = {22, 80}


def lambda_handler(event, context):
    try:
        sg_ids_with_open_port = []  # List of Security Groups with open ports

        # Retrieve all Security Groups
        sg_response = ec2_client.describe_security_groups()

        # Retrieve all running EC2 instances and their tags
        instance_response = ec2_client.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )

        # Processing EC2 instances
        instance_to_sg = {}  # Mapping instances to Security Groups
        instance_ports = {}  # Mapping instances to monitored ports
        instance_emails = {}  # Mapping instances to notification emails

        for reservation in instance_response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                sg_ids = [sg['GroupId'] for sg in instance['SecurityGroups']]

                # Retrieve instance tags
                tags = {tag["Key"]: tag["Value"] for tag in instance.get("Tags", [])}

                # Retrieve port list from the OpenPorts tag
                if "OpenPorts" in tags:
                    try:
                        ports_to_check = {int(p) for p in tags["OpenPorts"].split(",") if p.strip().isdigit()}
                    except ValueError:
                        ports_to_check = DEFAULT_PORTS
                else:
                    ports_to_check = DEFAULT_PORTS

                # Retrieve email list from the AlertEmails tag
                emails = tags.get("AlertEmails", "").split(",")
                emails = [email.strip() for email in emails if "@" in email]

                # Assign values to dictionaries
                instance_to_sg[instance_id] = sg_ids
                instance_ports[instance_id] = ports_to_check
                instance_emails[instance_id] = emails

        # Checking for open ports in Security Groups
        for sg in sg_response['SecurityGroups']:
            sg_id = sg['GroupId']

            for permission in sg.get('IpPermissions', []):
                if (
                    "FromPort" in permission and
                    "ToPort" in permission and
                    permission["FromPort"] == permission["ToPort"] and
                    any(ip.get("CidrIp") == "0.0.0.0/0" for ip in permission.get("IpRanges", []))
                ):
                    sg_ids_with_open_port.append((sg_id, permission["FromPort"]))

        # Filtering instances with open ports
        instances_to_report = []
        for instance_id, sg_ids in instance_to_sg.items():
            open_ports = {port for sg_id, port in sg_ids_with_open_port if sg_id in sg_ids and port in instance_ports[instance_id]}

            if open_ports:
                email_list = instance_emails.get(instance_id, [])
                if email_list:  # Send email only if notification emails exist
                    instances_to_report.append((instance_id, open_ports, email_list))

        # Sending email alerts
        if instances_to_report:
            subject = "AWS Security Alert: Open Ports on EC2 Instances"
            body = "The following EC2 instances have open ports accessible to the world (0.0.0.0/0):\n\n"

            for instance_id, open_ports, email_list in instances_to_report:
                body += f"Instance ID: {instance_id}\n"
                body += f"Open Ports: {', '.join(map(str, open_ports))}\n"
                body += f"Security Groups: {', '.join(instance_to_sg[instance_id])}\n"
                body += "\n"

            # Sending a bulk email to all notification email addresses
            all_email_list = list(set(email for _, _, email_list in instances_to_report for email in email_list))

            ses_client.send_email(
                Source=SES_SENDER_EMAIL,
                Destination={"ToAddresses": all_email_list},
                Message={
                    "Subject": {"Data": subject},
                    "Body": {"Text": {"Data": body}},
                },
            ) 

            print(f"Sent alert email for instances: {', '.join([instance_id for instance_id, _, _ in instances_to_report])} to {', '.join(all_email_list)}")
    except Exception as e:
        print(f"Error: {e}")
