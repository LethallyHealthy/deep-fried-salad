#!/usr/local/bin/python3

# Author: Mickey Somra
# Last Updated: 01/24/2018
# Purpose: This script will create a client to send from any IP or port;
#       it will also return the the message sent if the server is running

import socket
import time
import atexit
from socket import *

def exit_handler():
    print('closing')

# Get the server hostname, port and data length

hostname='128.235.217.98'
port=12001
userName='Fernando'
userInfo="1:" + userName
message= ""

# Create client socket. SOCK_DGRAM is used for UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(userInfo.encode(),(hostname, port))
messageRecv, address = clientSocket.recvfrom(4096)

atexit.register(exit_handler)
while (True):
    rawMessage=input("Enter message: ")
    if (rawMessage == "exit"):
        break
    
    messageSend = userName + ": " + rawMessage
    
    clientSocket.sendto(messageSend.encode(),(hostname, port))
    
    messageRecv, address = clientSocket.recvfrom(4096)
        

    print(messageRecv.decode())
        
#Close the client socket
clientSocket.close() 
