import sys
import socket

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
    # Send data image
    message = open("prediksi-harga-btt.png", 'rb')
    message_read = message.read()
    print(f"sending {message}")
    sock1.sendall(message_read)
    sock2.sendall(message_read)

    # Look for the response
    amount_received1 = 0
    amount_expected1 = len(message_read)
    amount_received2 = 0
    amount_expected2 = len(message_read)
    file1 = bytearray()
    while amount_received1 < amount_expected1:
        data1 = sock1.recv(256)
        amount_received1 += len(data1)
        file1 += data1
        print("Alpine 1: ", f"{data1}")

    #file respon dari alpine 1
    write1 = open("image1.jpg", 'wb')
    write1.write(file1)
    write1.close()

    file2 = bytearray()
    while amount_received2 < amount_expected2:
        data2 = sock2.recv(256)
        amount_received2 += len(data2)
        file2 += data2
        print("Alpine 2: ", f"{data2}")

    #file respon dari alpine 2
    write2 = open("image2.jpg", 'wb')
    write2.write(file2)
    write2.close()
finally:
    print("closing")
    sock1.close()
    sock2.close()