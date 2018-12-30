# import threading
# from threading import Thread
# from scapy.all import *

# packets = []

# def capture():
#     capture =  sniff(iface="Qualcomm Atheros AR922X Wireless Network Adapter",  prn = extract)
#     wrpcap('scapy.pcap', capture)


# def extract(packet):
#     global packets
#     if len(packets) == 30:
#         packets = []
#     while len(packets) != 30:
#         packet = "haha"# DUMMY PACKET TO DAPAT GANTO ITSURA[192.168.8.1,192.179.2.1,0, 'icmp', 'eco_i', 'SF', 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 4, 2, 0.5, 0.75, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 'nmap.']
#         packets.append(packet)
#     print(packet)
#     return packets

# c = Thread(target = capture)
# c.daemon = True
# c.start()