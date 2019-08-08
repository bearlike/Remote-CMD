import time, socket, sys, os, getopt

def main(server_host,name):
   os.system("cls")
   print('Client Server...')
   time.sleep(1)
   #Get the hostname, IP Address from socket and set Port
   soc = socket.socket()
   shost = socket.gethostname()
   ip = socket.gethostbyname(shost)
   #get information to connect with the server
   print(shost, '({})'.format(ip))
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
      message = message.decode().strip()
      if(message.upper() != "ACK") and (message != ""):
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
      if(message == "[kill server]"):
         exit(-1)


# Prints usage/help
def usageHelp():
   class TextColors:
      HEADER = '\033[95m'
      OKBLUE = '\033[94m'
      OKGREEN = '\033[92m'
      WARNING = '\033[93m'
      FAIL = '\033[91m'
      ENDC = '\033[0m'
      BOLD = '\033[1m'
      UNDERLINE = '\033[4m'
   print("Usage:\n  client.py ","<IPv4 Address of the server> <client preferred name>")
   sys.exit(2)


if __name__=="__main__":
   try:
      server_host, name = sys.argv[1:]
   except:
      usageHelp()
   try:
      socket.inet_aton(server_host)
   except socket.error:
      print("Invalid IP Address or Connection terminated")
      usageHelp()
   try:
      main(server_host,name)
   except ConnectionAbortedError:
      print("\nConnection Aborted: An established connection was aborted by the host machine. Maybe caused due to Server-side Exceptions")
   except ConnectionRefusedError:
      print("\nConnection Refused: No connection could be made because the target machine actively refused it")
      print("Recheck the IP address entered, check if the Server is online, allowed through firewall and Try again")