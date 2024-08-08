#6510405407 จิรายุ โออุไร
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
messageList = ""
topic = ""

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")

    if(topic == ""):
        connectionSocket.send("REQUEST_START_TOPIC".encode())
        topic = connectionSocket.recv(1024).decode()

    else:
        connectionSocket.send("PLAY_GAME".encode())
        initialRequest = connectionSocket.recv(1024).decode()
        if initialRequest == 'REQUEST_MESSAGE_LIST':
            connectionSocket.send((topic + " : " + messageList).encode())
    
    word = connectionSocket.recv(1024).decode()
    messageList += (" " + word + ", ") 

    connectionSocket.close()
