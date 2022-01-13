import subprocess
import json

data = subprocess.check_output(['ipconfig', '/all']).decode('utf-8').split('\n')

ip_config = {}


for item in data:
    if item.find('Host Name') != -1:
        ip_config['Host Name'] = item.split(':')[1]
        
    if item.find('IPv4 Address') != -1:
        ip_config['IPv4 Address'] = item.split(':')[1]
        
    if item.find('Subnet Mask') != -1:
        ip_config['Subnet Mask'] = item.split(':')[1]

print(json.dumps(ip_config))
