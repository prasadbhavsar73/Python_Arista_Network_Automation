from netmiko import ConnectHandler

dev= input("Enter IP of Network Device: ")
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

i= input("Enter Loopback Adapter Name: ")
j= input("Enter Loopback Adapter IP: ")
k= input("Enter Loopback Adapter Subnet Mask: ")

config_commands = ['int '+ i, 'ip address '+j+' '+k]
arista_execution.enable()
arista_execution.config_mode()
arista_execution.send_config_set(config_commands)
print ("\n"+i+" has been configured."+"\n")

ans=input("Would you like to verify the "+i+" configurations (yes/no)? ")

if (ans=="yes"):
      command = arista_execution.send_command('show ip interface br')
      print ("\n"+"Summary of the Interfaces: \n \n" + command+"\n")

else:
      print("\n"+"Thank you!")
