import json
from pyntc import ntc_device as NTC

device = NTC(host="10.100.2.178", username="reza", password="123", device_type="cisco_ios_ssh")
device.open()

ios_run = device.running_config
print(ios_run)

