# from scapy.all import *

# capture =  sniff(iface="Qualcomm Atheros AR922X Wireless Network Adapter",timeout=5)
# print(type(capture))
# print (capture)
# wrpcap('scapy.pcap', capture)

# #source destination duration protocol flags
# #print (capture[2])           #A binary file, a simple capture element

# print (capture[2].show())
# print ("Source: " + capture[2][IP].src)           #source IP
# print ("Destination: " + capture[2][IP].dst)      #destination IP
# print (capture[2][IP].ttl)                        #Time to Live = Duration??
# print (capture[2].proto)                      #Protocol
# print (capture[2][IP].flags)                      #Plag