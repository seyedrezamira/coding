from napalm import get_network_driver
import json

driver = get_network_driver("nxos_ssh")
device = driver("10.100.2.186", "reza", "123")
device.open()

output1 = device.get_facts()
print (json.dumps(output1, indent = 4))

output2 = device.get_arp_table()
print (json.dumps(output2, indent = 4))

