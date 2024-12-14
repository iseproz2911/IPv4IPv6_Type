# menu.py 
import socket
import struct 

# Function Send Unicast(IPv4)
def send_unicast_ipv4(message, target_ip, target_port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(message.encode(), (target_ip, target_port))
        
# Function Send Broadcast(IPv4)
def send_broadcast_ipv4(message, target_port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(message.encode(), ('255.255.255.255', target_port))
        
#Function Send Multicast(IPv4)
def send_multicast_ipv4(message, group_ip, group_port):
    multicast_group = (group_ip, group_port)
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
        ttl = struct.pack('B', 255)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
        s.sendto(message.encode(), multicast_group)
        
#Function Send Anycast(IPv4)
def send_anycast_ipv4(message, target_ips, target_port):
    for ip in target_ips:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(message.encode(), (ip, target_port))
            print(f"Send Message Anycast to {ip}:{target_port}")

#Function Send Unicast(IPv6)
def send_unicast_ipv6(message, target_ip, target_port):
    with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as s:
        s.sendto(message.encode(), (target_ip, target_port))    
        
#Function Send Multicast(IPv6)
def send_multicast_ipv6(message, group_ip, target_port):
    multicast_group = (group_ip, target_port)
    with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as s:
        ttl = struct.pack('B', 255)
        s.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, ttl) 
        s.sendto(message.encode(), multicast_group)

#Function Send Anycast(IPv6)
def send_anycast_ipv6(message, target_ips, target_port):
    for ip in target_ips:
        with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as s:
            s.sendto(message.encode(), (ip, target_port))
            print(f"Send Message Anycast to {ip}:{target_port}")
            
#Main Menu
def menu():
    print("Slect 1-6:")
    print("1. Send Unicast")
    print("2. Send Broadcast")
    print("3. Send Multicast")
    print("4. Send Anycast (IPv4)")
    print("5. Send Anycast (IPv6)")
    print("6. Exit")
    
    choice = input("Choose 1-6: ")
    
    if choice == '1':
        print("Sent Unicast")
        target_ip = input("IP target: ")
        target_port = int(input("Port target: "))
        message = input("Input Message: ")
        return 'unicast', target_ip, target_port, message
    elif choice == '2':
        print("Sent Broadcast")
        target_port = int(input("Port target: "))
        message = input("Input Message: ")
        return 'broadcast',None , target_port, message
    elif choice == '3':
        print("Sent Multicast")
        group_ip = input("Input GroupIPv4 Multicast: ")
        target_port = int(input("Port target: "))
        message = input("Input Message: ")
        return 'multicast', group_ip, target_port, message
    elif choice == '4':
        print("Sent Anycast (IPv4)")
        target_ips = input("Input GroupIPv4:").split()
        target_port = int(input("Port target: "))
        message = input("Input Message: ")
        return 'anycast_ipv4', target_ips, target_port, message
    elif choice == '5':
        print("Sent Anycast (IPv6)")
        target_ips = input("Input GroupIPv6: ").split()
        target_port = int(input("Port target: "))
        message = input("Input Message: ")
        return 'anycast_ipv6', target_ips, target_port, message
    elif choice == '6':
        print("Exit.")
        return None, None, None, None
    else:
        print("404")
        return menu() 