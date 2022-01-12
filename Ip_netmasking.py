import socket
import json

hostname = socket.gethostname()

ip_address = socket.gethostbyname(hostname)

subnetmask = ".".join(ip_address.split(".")[:3])

ip = {"hostname" : hostname, "ip_address" : ip_address, "sub_net_mask" : subnetmask}

print(json.dumps(ip))
