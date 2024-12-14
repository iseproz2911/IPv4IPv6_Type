import socket
import struct
MCAST_GRP = 'ff02::1:1:1'
# MCAST_GRP = '224.12.1.1'
MCAST_PORT = 50321
IS_ALL_GROUPS = True
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if IS_ALL_GROUPS:
        sock.bind(('', MCAST_PORT))
else:
        sock.bind((MCAST_GRP, MCAST_PORT))

mreq = struct.pack("16sI", socket.inet_pton(socket.AF_INET6,MCAST_GRP), 0)
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)

# mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
        print(sock.recv(10240))