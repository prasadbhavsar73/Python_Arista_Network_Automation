from netmiko import ConnectHandler

dev= input("Enter IP Address of Network Device: ")
un= input("Enter Username: ")
pwd= input("Enter the Password: ")

Arista_VM = {
      'device_type': 'arista_eos',
      'ip': dev,
      'username': un,
      'password': pwd,
}

arista_execution = ConnectHandler(**Arista_VM)

print(" \n"+"You've successfully connected to the Network Device. \n \n")

command1 = arista_execution.find_prompt()
print ("Current Command Mode: \n \n" +command1+"\n")

command2 = arista_execution.send_command('show version')
print ("Device Version Information: \n \n" + command2+"\n")

command3 = arista_execution.send_command('show interfaces')
print ("Statistics of the Network Interfaces: \n \n" + command3+"\n")

command4 = arista_execution.send_command('show ip interface br')
print ("Summary of the Interfaces: \n \n" + command4+"\n")

command5 = arista_execution.send_command('show ip route summary')
print ("Route Summary Information: \n \n" + command5+"\n")

