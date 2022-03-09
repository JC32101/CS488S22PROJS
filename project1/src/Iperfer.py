import sys
import socket

print(len(sys.argv))
if(len(sys.argv) > 4 or len(sys.argv) < 4 ):
  exit("Error: missing or additional arguments")
elif(int(sys.argv[2]) < 1025 or int(sys.argv[2]) > 65534):
  exit("Error: port number must be in the range 1024 to 65535")


ServerName = sys.argv[1]
ServerPort = sys.argv[2]
Time = sys.argv[3]
ServerAddress = (ServerName, ServerPort)
print(ServerAddress, Time)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(ServerAddress)

while 1:
    
    # Create message
    message = input('Enter the lower case message: ')

    # Send message
    clientSocket.send(message.encode("utf-8"))

    # Receive from server
    modified_sent = clientSocket.recvfrom(2048)

    # Print received message
    print("From server:", modified_sent)
    
    continue

# Close connection
clientSocket.close()

try:
  clientSocket.connect(ServerAddress)
    #recv = s.recv(1024).decode()
    #s.close()
  for i in Time:
    # Create message
    message = input('Enter the lower case message: ')

    # Send message
    clientSocket.send(message.encode("utf-8"))

    # Receive from server
    modified_sent = clientSocket.recvfrom(2048)

    # Print received message
    print("From server:", modified_sent)
    
    continue
except socket.error as err:
   print(err)
