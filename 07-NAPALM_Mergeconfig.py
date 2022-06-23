import json
from napalm import get_network_driver

driver = get_network_driver('ios')
device = driver("10.100.2.178", "reza", "123")
device.open()
print("Accessing to 10.100.2.178")
device.load_merge_candidate(filename="ACL.cfg")
device.commit_config()
device.close()


