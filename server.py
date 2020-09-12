#!/usr/bin/env python3
import time, socket, sys, os
from pathlib import Path

# Driver Code
def main():
   os.system("cls")
   try:
      os.mkdir(".cache")
   except FileExistsError:
      pass
   print('Setup Server...')
   time.sleep(1)
   # Get the hostname, IP Address from socket and set Port
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
   print("Received connection request from ", addr[0], "("+ str(addr[1])+ ")\n")
   print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
   programPath = os.getcwd()
   #get a connection from client side
   client_name = connection.recv(1024)
   client_name = client_name.decode()
   print(client_name + ' has connected.')
   connection.send(name.encode())
   message = "ACK"
   # Main Loop
   while True:
      connection.send(message.encode())
      message = "ACK"
      # If connections problem occurs
      try:
         message = connection.recv(1024)
         message = message.decode()
         print(client_name, '(remote)>', message)
      except (ConnectionResetError, ConnectionAbortedError, ConnectionRefusedError, ConnectionError) as errorConnetion:
         print(errorConnetion,"\n"+(client_name).strip()+" has terminated connection")
         print(client_name + " has terminated connection")
         soc.listen(1)  # Try to locate using socket
         print('Waiting for incoming connections...')
         connection, addr = soc.accept()
         print("Received connection request from ", addr[0], "("+ str(addr[1])+ ")\n")
         print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
         client_name = connection.recv(1024)
         client_name = client_name.decode().strip()
         print(client_name + ' has connected.')
         connection.send(name.encode())
         message = "ACK"
         continue
      # Kill server from remote
      if message == "[kill server]":
         print("Killing server upon ["+client_name+"] request")
         exit(-1)
      # For Quit
      if message == "[quit]":
         print(client_name + " has terminated connection")
         soc.listen(1)  # Try to locate using socket
         print('Waiting for incoming connections...')
         connection, addr = soc.accept()
         print("Received connection request from ", addr[0], "("+ str(addr[1])+ ")\n")
         print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
         client_name = connection.recv(1024)
         client_name = client_name.decode()
         print(client_name + ' has connected.')
         connection.send(name.encode())
         message = "ACK"
         continue
      # Default
      elif(message!="cls") or (message!="[quit]") or (message!=""):
         if(message[:2]=="cd"):
            try:
               os.chdir(message[2:].strip())
               message = "Current Path is "+str(os.getcwd())
            except OSError:
               message = "The filename, directory name, or volume label syntax is incorrect"
               print(message)
            continue
         elif (message=="dir") or (message=="ls"):
            tempVar = os.listdir()
            message=("\n Directory of "+str(os.getcwd())+"\n\n")
            for temp in tempVar:
               message=message+str(temp)+"\n"
            continue
         message = message +" > .cache/temp.txt"
         status = str(os.system(message))
         if(status != '0'):
            message = "Unable to execute command!"
            print(message)
            continue
         textPath = str(programPath+"//.cache//temp.txt").replace("\\","//")
         # print(textPath)
         message = "ACK"
         my_file = Path(textPath)
         if my_file.is_file():
            with open(textPath, "r") as f:
               message = f.read()
            os.system("rm "+textPath)
            if message != "":
               print((time.strftime('%d/%m/%Y %H:%M:%S')),message)
            else:
               message = "ACK"
         else:
            message = "ACK"
      # If Exception case
      else:
         message = "ACK"

if __name__=="__main__":
   try:
      main()
   except KeyboardInterrupt:
      print("KeyboardInterrupt Encountered")