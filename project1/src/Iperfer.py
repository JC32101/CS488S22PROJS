# track how much data was sent during that time frame
import sys
import socket
import time

if (len(sys.argv) > 4 or len(sys.argv) < 4):
    print("Error: missing or additional arguments")
elif (int(sys.argv[2]) < 1025 or int(sys.argv[2]) > 65534):
    print("Error: port number must be in the range 1024 to 65535")

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
time = int(sys.argv[3])
serverAddress = (serverName, serverPort)
bit = 0
message = "1"

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  clientSocket.connect(serverAddress)
  endtime = time.time() + time
  while (time.time() < endtime):
    
    # Send message
    clientSocket.send(message.encode("utf-8"))
    bit=bit+1000
    
    # Receive from server
    modified_sent = clientSocket.recvfrom(2048)

  # Close connection
  clientSocket.close()
    
  #Print Bandwidth
  bandwidth = (bit/1000000)/time
  print("Bandwidth: " + bandwidth + " Mbps")
except socket.error as err:
  print(err)


