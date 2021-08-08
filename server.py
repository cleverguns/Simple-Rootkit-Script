#SERVER DEMO

import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1' #my ip add you use 127.0.0.1
port = 1234             #port for data transfering

server.bind( (host,port) ) # Bind Server
server.listen(5)

run = True
client, addr = server.accept()
print ('Connection from', addr)

while run:
   try:
        data = input('>>>')
        client.send (data.encode('UTF-8'))    #send to client
        
        
        msg = client.recv(1024)                     #Recieve data
        print (msg.decode('UTF-8'))
   except ConnectionResetError:
        print('Client lost. Trying to connect . . .')
        client, addr = server.accept()
        print('Go Connection from', addr) 
