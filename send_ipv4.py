from menu import menu, send_unicast_ipv4, send_broadcast_ipv4, send_multicast_ipv4, send_anycast_ipv4
def send_ipv4():
    action, target_ip, target_port, message = menu()
    
    if action == 'unicast':
        send_unicast_ipv4(message, target_ip, target_port)
        print(f"Sent Message Unicast: {message} to {target_ip}:{target_port}")
    elif action == 'broadcast':
        send_broadcast_ipv4(message, target_port)
        print(f"Sent Message Broadcast: {message}")
    elif action == 'multicast':
        send_multicast_ipv4(message, target_ip, target_port)
        print(f"Sent Message Multicast: {message} to Group {target_ip}:{target_port}")
    elif action == 'anycast_ipv4':
        send_anycast_ipv4(message, target_ip, target_port)
        print(f"Sent Message Anycast IPv4: {message} to ... {', '.join(target_ip)}:{target_port}")
    elif action is None:
        print("End.")

if __name__ == "__main__":
    send_ipv4()
