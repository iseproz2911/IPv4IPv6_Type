# ipv6_sender.py
from menu import menu, send_unicast_ipv6, send_multicast_ipv6, send_anycast_ipv6

def send_ipv6():
    action, target_ip, target_port, message = menu()
    
    if action == 'unicast':
        send_unicast_ipv6(message, target_ip, target_port)
        print(f"Sent Message Unicast IPv6: {message} to {target_ip}:{target_port}")
    elif action == 'multicast':
        send_multicast_ipv6(message, target_ip, target_port)
        print(f"Sent Message Multicast IPv6: {message} to group {target_ip}:{target_port}")
    elif action == 'anycast_ipv6':
        send_anycast_ipv6(message, target_ip, target_port)
        print(f"Sent Message Anycast IPv6: {message} to ... {', '.join(target_ip)}:{target_port}")
    elif action == 'broadcast':
        print("Error! IPv6 does not suppo   rt!")
    elif action is None:
        print("End")

if __name__ == "__main__":
    send_ipv6()
