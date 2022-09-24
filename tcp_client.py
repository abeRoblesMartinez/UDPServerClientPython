# TCP server/client
import socket
import socket
serverPort = 12000
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1',serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print ('From TCP Server:', modifiedSentence.decode())
clientSocket.close()
