#server module, launch first

import socket
import gameboard

serverAddress = '127.0.0.1'
port = 8000 #server port
aSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
aSocket.bind((serverAddress, port)) #bind host with port number

aSocket.listen(1) #allows only 1 connection
bSocket, bAddress = aSocket.accept()

clientmsg = bSocket.recv(1024).decode('ascii')#receive connect msg
print(clientmsg)
gameboard.whichUser = 2
gameboard.pSocket = bSocket


gb = gameboard.BoardClass()