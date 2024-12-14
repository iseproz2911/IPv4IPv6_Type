import socket
# MCAST_GRP = 'ff02::1:1:1'
MCAST_GRP = '224.12.1.1'
MCAST_PORT = 50021
MULTICAST_TTL = 2

# sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, MULTICAST_TTL)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

sock.sendto(b"Multicast IPv4 for Member ff02::1:1:1", (MCAST_GRP, MCAST_PORT))