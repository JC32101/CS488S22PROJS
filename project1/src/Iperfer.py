# track how much data was sent during that time frame

import sys
import socket
import time

PacketByte = bytes(0)
Throughput = 0

#print(len(sys.argv))
if (len(sys.argv) > 4 or len(sys.argv) < 4):
    exit("Error: missing or additional arguments")
elif (int(sys.argv[2]) < 1025 or int(sys.argv[2]) > 65534):
    exit("Error: port number must be in the range 1024 to 65535")

ServerName = sys.argv[1]
ServerPort = int(sys.argv[2])
Time = int(sys.argv[3])
ServerAddress = (ServerName, ServerPort)
#print(ServerAddress, Time)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

message = b"0" * 1000

try:
    clientSocket.connect(ServerAddress)
    endtime = time.time() + 10
    while (time.time() < endtime):

        # Send message
        clientSocket.send(message.encode("utf-8"))

        # Receive from server
        PacketByte = bytes(clientSocket.recvfrom(2048))

        # Print received message
        print("From server:", PacketByte)

        continue
      
except socket.error as err:
    print(err)

#Throughput = PacketByte / endtime #data sent/time elapsed
#print("Throughput: " + Throughput + " Mbps")

# Close connection
clientSocket.close()
