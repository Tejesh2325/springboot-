import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="ami-068257025f72f470d",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="ansible"
    )