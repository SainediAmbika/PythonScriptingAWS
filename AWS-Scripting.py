import boto3

ec2 = boto3.resource('ec2')

# Instance Launching
# Comment the below part while terminating the instance

instance = ec2.create_instances(
    ImageId='ami-087f352c165340ea1',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    # Tags used for giving Instance name
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'MyPythonInstance'
                }
            ]
        }
    ]
)

print(instance[0].id)


# Terminating an instance
# Comment the above part while creating the instance

# instance_id='i-036a6f1abc2dee4f3' # check in aws for instance id
# instance=ec2.Instance(instance_id)
# response=instance.terminate()
# print(response)