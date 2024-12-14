# IPv4IPv6_Type
IPv4/IPv6 Unicast, Multicast, Broadcast, Anycast
In this topic, we will build a system using three Raspberry Pi devices pre-installed with WebOS, connected via a LAN network. The focus will be on sending and receiving messages using different communication methods like Unicast, Multicast, Broadcast, and Anycast.

Tasks

1. System Setup
Configure a system of three Raspberry Pi devices, each connected through a LAN network and running WebOS.

2. IPv4 Communication
Develop Python programs to send and receive messages using IPv4 communication methods:
Unicast: Direct communication between two specific devices.
Broadcast: Messages sent to all devices in the network.
Multicast: Messages sent to a specific group of devices using IGMP (Internet Group Management Protocol).

3. IPv6 Communication
Develop Python programs to send and receive messages using IPv6 communication methods:
Unicast: Direct communication between two specific devices.
Multicast: Messages sent to a specific group of devices.
Anycast: Messages sent to the nearest device in a group.

5. Performance and Security Evaluation
Evaluate the performance and security of each communication method and make a recommendation based on their suitability for sending and receiving messages.
Multicast Configuration
Device 1:
Assign an IP address: 10.12.1.11/24.
Add the device to the multicast group 224.0.0.0.
Restart the network manager to apply changes.

Device 2:
Assign an IP address: 10.12.1.22/24.
Add the device to the multicast group 224.0.0.0.
Enable ICMP echo reply for broadcast messages.
Restart the network manager to apply changes.

Device 3:
Assign an IP address: 10.12.1.33/24.
Add the device to the multicast group 224.0.0.0.
Enable ICMP echo reply for broadcast messages.
Restart the network manager to apply changes.

Multicast Group Verification
To ensure all devices have joined the multicast group, verify the multicast configuration:
Check the network interfaces for multicast support.
Ensure multicast is enabled on the eth0 interface.

Testing Multicast
On Device 1 (Sender):
Test that Devices 2 and 3 have joined the multicast group by sending a ping request to the multicast address 224.0.0.1.
If Devices 2 and 3 respond, the multicast group setup is successful.

Report Result:
https://hackmd.io/@iamproz2911/Hy8__6PNkg
