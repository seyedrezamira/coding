import json
from pyntc import ntc_device as NTC

device = NTC(host="10.100.2.178", username="reza", password="123", device_type="cisco_ios_ssh")
device.open()
ios_output = device.facts
device.config_list(["hostname switch", 
                    "router ospf 1",
                    "network 0.0.0.0 255.255.255.255 area 0",
                    "network 10.10.10.0 0.0.0.255 area 10"
                    ])



