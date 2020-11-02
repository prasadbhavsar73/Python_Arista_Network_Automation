from netmiko import ConnectHandler

dev= input("Enter IP of the Device: ")
un= input("Enter Username: ")
pwd= input("Enter Password: ")

Arista_VM = {
    'device_type': 'arista_eos',
    'ip': dev,
    'username': un,
    'password': pwd,
}

arista_execution = ConnectHandler(**Arista_VM)

print(" \n"+"You've successfully connected to the Network Device. \n \n")

first =int(input("Enter the first VLAN: "))
last1 =int(input("Enter the last VLAN: "))
last2=last1+1

print(" \n"+"Please wait VLANs creation is in progress, do not close the terminal! \n")

for n in range (first, last2):
         print ("Creating VLAN " + str(n))
         arista_execution.enable()
         arista_execution.config_mode()
         config_commands = ['vlan ' + str(n), 'name VLAN_' + str(n)]
         arista_execution.send_config_set(config_commands)

command = arista_execution.send_command('show vlan')
print ("\n"+"VLAN Summary on the device "+dev+" : \n \n" + command+"\n")

arista_execution.disconnect()
~
