import re
import paramiko
import time

ip_address = "10.100.2.178"
username = "reza"
password = "123"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username, password=password)

print(f"succesful connection to {ip_address}")

remote_connection = ssh_client.invoke_shell()
remote_connection.send("configure terminal\n")
remote_connection.send("int loo 1\n")
remote_connection.send("ip add 1.1.1.1 255.255.255.255\n")

