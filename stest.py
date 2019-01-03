from socket import * 
serverName="10.1.10.18"
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(3)
print 'Server is ready'
count=1
myfile1 = open("psutil-5.4.8.tar.gz", 'rb')
bytes = myfile1.read()
myfile1.close()
while 1:
	connectionSocket,addr=serverSocket.accept()
	print("Total bytes:",len(bytes))
	connectionSocket.sendall(str(len(bytes)))
	ack1=connectionSocket.recv(1024)
	print(ack1)
	connectionSocket.sendall(bytes)

	
	
	
	
	
	
	
	
	
	
	
	
