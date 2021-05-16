import sys
import socket
import random
import string

# Create a TCP/IP socket
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address1 = ('192.168.122.243', 10000)
server_address2 = ('192.168.122.130', 10000)
print(f"connecting to {server_address1}")
print(f"connecting to {server_address2}")
sock1.connect(server_address1)
sock2.connect(server_address2)


try:
    # Send data
    message1 = '' . join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2000000))
    message2 = '' . join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2000000))
    print(f"sending {message1}")
    print(f"------------------")
    print(f"sending {message2}")
    sock1.sendall(message1.encode())
    sock2.sendall(message2.encode())
    # Look for the response
    amount_received1 = 0
    amount_expected1 = len(message1)
    amount_received2 = 0
    amount_expected2 = len(message2)
    
    while amount_received1 < amount_expected1:
        data1 = sock1.recv(256)
        amount_received1 += len(data1)
        print(f"{data1}")

    while amount_received2 < amount_expected2:
        data2 = sock2.recv(256)
        amount_received2 += len(data2)
        print(f"{data2}")
finally:
    print("closing")
    sock1.close()
    sock2.close()
