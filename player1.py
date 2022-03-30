#client module

import gameboard
import socket

def startConnection():
    serverAddress = input('Enter the IP: ') #'127.0.0.1'
    serverPort = int(input('Enter the port: '))#8000
    try:
        aSocket.connect((serverAddress, serverPort))
        gameboard.pSocket = aSocket
    except ConnectionRefusedError:
        retryConnection = input('Do you want to try connecting again? ')
        if retryConnection == 'y':
            startConnection()
        elif retryConnection == 'n':
            quit()
        else:
            print('Not an option, terminating program because the instructions don\'t ask for anything if y or n isn\'t entered :p')
            quit()

if __name__ == '__main__':
    aSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    startConnection()
    '''
    aSocket.connect(('127.0.0.1', 8000))
    gameboard.pSocket = aSocket
    '''
    gameboard.whichUser = 1
    print('Connected!')
    aSocket.send(b'Connected!')
    gameboard.turn = True
    gb = gameboard.BoardClass()