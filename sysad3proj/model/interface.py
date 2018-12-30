import subprocess
import os
#wmic.exe nicconfig where "IPEnabled  = True" get ipaddress,MACAddress,IPSubnet,DNSHostName,Caption,DefaultIPGateway /format:rawxml
def getInterface():
    output = subprocess.check_output("ipconfig/all", shell=True).decode('utf-8')
    output = str(output)
    split = output.split("\n")
    wireless = output[output.find("Wireless LAN adapter WiFi:"):]
    print(wireless)
    split = wireless.split("\n")
    desc = split[3]
    name = desc[desc.find(":")+2:]
    print(name)
    return name

getInterface()