import sys
import socket
import time

if (len(sys.argv) != 4):
    print("Error: missing or additional arguments")
elif (int(sys.argv[2]) < 1025 or int(sys.argv[2]) > 65534):
    print("Error: port number must be in the range 1024 to 65535")

ServerName = sys.argv[1]
ServerPort = int(sys.argv[2])
Time = int(sys.argv[3])
ServerAddress = (ServerName, ServerPort)
byte = 0
message = bytes(1000)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  clientSocket.connect(ServerAddress)
  endtime = time.time() + Time
  while (time.time() < endtime):
    clientSocket.send(message.encode("utf-8"))
    
    modified_sent = clientSocket.recvfrom(2048)
    
    byte=len(modified_sent[0])
  Throughput = byte/(Time*125000)
  print("sent="+str(bit/1000)+"KB rate="+str(Throughput)+"Mbps")
except socket.error as err:
  print(err)

clientSocket.close()