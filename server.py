import socket
import threading
import time
import sys

def reconnect_to_server(host, port):
    while True:
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((host, port))
            return server_socket
        except:
            print(f"Failed to reconnect to {host}:{port}. Retrying in 5 seconds...")
            time.sleep(5)

def handle_client(client_socket):
    try:
        client_name = client_socket.recv(1024).decode()
        print(f"Client connected: {client_name}")
        
        clients.append((client_name, client_socket))
        
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"{client_name}: {message}")

            ms = message.split()

            if "RESEND" in ms:
                new_ms = ""
                for val in ms:
                    if val != "RESEND":
                        new_ms = new_ms + val + " "

                for name, client in clients:
                    if client != client_socket:
                        client.send(f"{new_ms}".encode())

            else: 
                for name, client in clients:
                    if client != client_socket:
                        client.send(f"{client_name}: {message}".encode())

                #enviar el mensaje al otro servidor
                server2_socket.send(f"RESEND {client_name}: {message}".encode())
                
    except Exception as e: 
        print(e)
        pass
    
    print(f"Client disconnected: {client_name}")
    clients.remove((client_name, client_socket))
    client_socket.close()

clients = []

if len(sys.argv) != 3:
    print("Usage: python server.py <server_port> <server_port_other_server>")
    sys.exit(1)

# Configuración del servidor 1
server2_host = 'localhost'
server2_port = int(sys.argv[1])


server1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server1_socket.bind(('0.0.0.0', int(sys.argv[2])))
server1_socket.listen(5)

server2_socket = reconnect_to_server(server2_host, server2_port)

#print("Server 1 listening on port 8001")

while True:
    client_socket, client_address = server1_socket.accept()
    print("Accepted connection from:", client_address)
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
