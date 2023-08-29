import socket
import threading
import sys

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("Error receiving messages.")
            break

def send_messages(client_socket):
    while True:
        try:
            message = input()
            client_socket.send(message.encode())
        except:
            print("Error sending messages.")
            break

if len(sys.argv) != 4:
    print("Usage: python client.py <server_ip> <server_port> <client_name>")
    sys.exit(1)

server_ip = sys.argv[1]
server_port = int(sys.argv[2])
client_name = sys.argv[3]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

print("Welcome to chat 😎\n")

# Enviar el nombre del cliente al servidor
client_socket.send(client_name.encode())

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
send_thread = threading.Thread(target=send_messages, args=(client_socket,))

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()

client_socket.close()
