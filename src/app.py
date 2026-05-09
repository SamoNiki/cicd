environment = "prod"
region = "eu-west1"
instance_count = 5

base_hostname = f"app-server{environment}-{region}"
print(base_hostname)