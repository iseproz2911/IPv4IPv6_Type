from scapy.all import Ether, IP, sendp

ether = Ether(dst="ff:ff:ff:ff:ff:ff")

ip = IP(dst="192.168.1.255")

packet = ether / ip
sendp(packet, iface="eth0") 