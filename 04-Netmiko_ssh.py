
from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'host': '10.100.2.178',
    'username': 'reza',
    'password': '123',
    }
R2 = {
    'device_type': 'cisco_ios',
    'host': '10.100.2.179',
    'username': 'reza',
    'password': '123',
    }

with open("config_files") as f:
    lines = f.read().splitlines()

all_devices = [R1,R2]
for line in all_devices:
    net_connect = ConnectHandler(**line)
    output = net_connect.send_config_set(lines)
    print (output)

