# track how much data was sent during that time frame
import sys
import socket
import time

#print(len(sys.argv))
if (len(sys.argv) > 4 or len(sys.argv) < 4):
    print("Error: missing or additional arguments")
elif (int(sys.argv[2]) < 1025 or int(sys.argv[2]) > 65534):
    print("Error: port number must be in the range 1024 to 65535")

ServerName = sys.argv[1]
ServerPort = int(sys.argv[2])
Time = int(sys.argv[3])
ServerAddress = (ServerName, ServerPort)
Throughput = 0
bit = 0
message = "1"


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  clientSocket.connect(ServerAddress)
  endtime = time.time() + Time
  while (time.time() < endtime):
    
    # Send message
    clientSocket.send(message.encode("utf-8"))
    bit=bit+1000
    
    # Receive from server
    modified_sent = clientSocket.recvfrom(2048)

  # Close connection
  clientSocket.close()
  Throughput = (bit/1000000)/Time #data sent/time elapsed
  print("Throughput: " + Throughput + " Mbps")
except socket.error as err:
  print(err)


