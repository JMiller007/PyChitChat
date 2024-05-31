import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on

# List to keep track of connected clients
clients = []

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                broadcast(message, client_socket)
            else:
                remove(client_socket)
                break
        except:
            remove(client_socket)
            break

# Function to broadcast messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)

# Function to remove disconnected clients
def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# Main function to start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server started on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"Connection established with {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()
