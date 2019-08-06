import time, socket, sys, os
os.system("cls")
print('Client Server...')
time.sleep(1)
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
#get information to connect with the server
print(shost, '({})'.format(ip))
server_host = "192.168.56.1" #input('Enter server\'s IP address:')
name = "kk" #input('Enter Client\'s name: ')
port = 1234
print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)
soc.connect((server_host, port))
print("Connected to Server.\n")
soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()
print('Enter [quit] to exit.')
while True:
   message = soc.recv(1024)
   message = message.decode()
   if(message != "ACK"):
      print(server_name, ">", message)
   message = input(str("Me > "))
   if message == "[quit]":
      soc.send(message.encode())
      print("\n")
      break
   elif message == "cls":
      os.system("cls")
      print("Enter [quit] to exit.\n")
   soc.send(message.encode())
