import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []

print("Server started...")

# Broadcast messages to all clients
def broadcast(message):

    for client in clients:

        try:
            client.send(message)

        except:
            pass

# Handle individual client
def handle(client):

    while True:

        try:

            message = client.recv(1024)

            if not message:
                break

            broadcast(message)

        except:
            break

    if client in clients:

        index = clients.index(client)

        clients.remove(client)

        client.close()

        username = usernames[index]

        usernames.remove(username)

        broadcast(f"{username} left the chat!".encode())

# Receive new clients
def receive():

    while True:

        client, address = server.accept()

        print(f"Connected with {str(address)}")

        client.send("USERNAME".encode())

        username = client.recv(1024).decode()

        usernames.append(username)

        clients.append(client)

        print(f"{username} joined!")

        broadcast(f"{username} joined the chat!".encode())

        client.send("Connected to server!".encode())

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()