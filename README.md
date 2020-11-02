Script1.py

Python program using Netmiko library to get the following information from Arista Switches.
•	Current Command Mode (EXEC/Privileged EXEC/Global Configuration/Interface Configuration)?
•	Version (Command: > show version)
•	Statistics Information of the Interfaces (Command: > show interfaces)
•	Summary of the Interfaces (Command:  > show ip interface brief)
•	Route Summary Information (Command: > show ip route summary)


Script2.py

Python program using Netmiko library to set up Loopback Adapters with IP Addresses on all three Arista Switches. Set the Loopback Adapters as follows.
•	Arista 1: Loopback 1 (IP Address: 1.1.1.1) 
•	Arista 2: Loopback 2 (IP Address: 2.2.2.2)
•	Arista 3: Loopback 3 (IP Address: 3.3.3.3)
At the end of the Script, add a condition to verify the Loopback Adapters configurations.


Script3.py

Python program using Netmiko library to set up VLANs all three Arista Switches. Set the VLANS as follows.
•	Arista 1: VLAN 1 to VLAN 2
•	Arista 2: VLAN 1 to VLAN 4
•	Arista 3: VLAN 1 to VLAN 6
At the end of the Script, add a condition to display the result of VLAN summary.
