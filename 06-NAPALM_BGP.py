from napalm import get_network_driver
import json

leaf_switches = ["10.100.2.186","10.100.2.187","10.100.2.188","10.100.2.189"]
for devices in leaf_switches:
    print ("Connecting to ", str(devices))
    driver = get_network_driver("nxos_ssh")
    device = driver(devices, "reza", "123")
    device.open()
    bgp_neighbors = device.get_bgp_neighbors()
    print (json.dumps(bgp_neighbors, indent = 4))
    device.close()




