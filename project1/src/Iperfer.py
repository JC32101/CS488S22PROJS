import sys
import socket
import time

if (len(sys.argv) != 4):
    print("Error: missing or additional arguments")
elif (int(sys.argv[2]) < 1025 or int(sys.argv[2]) > 65534):
    print("Error: port number must be in the range 1024 to 65535")

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
inputTime = int(sys.argv[3])
serverAddress = (serverName, serverPort)
byte = 0

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  clientSocket.connect(serverAddress)
  endTime = time.time() + inputTime
  count=0
  while time.time()<endTime:
    message = bytes(1000)
    clientSocket.send(message)
    count=count+1
    # modified_sent = clientSocket.recvfrom(2048)
    
  clientSocket.close()
except socket.error as err:
  print(err)

print("sent={} KB".format(count))
print("rate={} Mbps".format((count*8/(1000*inputTime))))
