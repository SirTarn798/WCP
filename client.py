#6510405407 จิรายุ โออุไร#6510405407 จิรายุ โออุไร
from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

init_status = clientSocket.recv(1024).decode()

if(init_status == "REQUEST_START_TOPIC"):
    topic = input("Pick a topic : ")
    clientSocket.send(topic.encode())
else:
    messageList = 'REQUEST_MESSAGE_LIST'
    clientSocket.send(messageList.encode())
    messageList = clientSocket.recv(1024).decode()
    print(messageList)

sentence = input('Insert a message to archive: ')
clientSocket.send(sentence.encode())
clientSocket.close()
