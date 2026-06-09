import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import simpledialog
from tkinter import filedialog
from plyer import notification
from encryption import encrypt_message, decrypt_message
from database import save_message

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Main Window
window = tk.Tk()
window.withdraw()

username = simpledialog.askstring("Login", "Enter Username")

window.deiconify()

window.title(f"Advanced Chat App - {username}")
window.geometry("600x600")

# Chat Area
chat_area = scrolledtext.ScrolledText(window)
chat_area.pack(padx=10, pady=10)

# Message Entry
message_entry = tk.Entry(window, width=40)
message_entry.pack(side=tk.LEFT, padx=10, pady=10)

# Send Message
def write():

    message = message_entry.get()

    if message != "":

        full_message = f"{username}: {message}"

        encrypted = encrypt_message(full_message)

        client.send(encrypted)

        save_message(username, message)

        message_entry.delete(0, tk.END)

# File Sharing
def send_file():

    filepath = filedialog.askopenfilename()

    if filepath:

        file_message = f"{username} shared file: {filepath}"

        encrypted = encrypt_message(file_message)

        client.send(encrypted)

# Receive Messages
def receive():

    while True:

        try:

            message = client.recv(1024)

            try:
                decoded_message = decrypt_message(message)

            except:
                decoded_message = message.decode()

            if decoded_message == "USERNAME":

                client.send(username.encode())

            else:

                chat_area.insert(tk.END, decoded_message + "\n")

                notification.notify(
                    title="New Message",
                    message=decoded_message,
                    timeout=3
                )

        except:

            print("Connection Error")

            client.close()

            break

# Buttons
send_button = tk.Button(window, text="Send", command=write)
send_button.pack(side=tk.LEFT)

file_button = tk.Button(window, text="Share File", command=send_file)
file_button.pack(side=tk.LEFT)

# Thread
receive_thread = threading.Thread(target=receive)
receive_thread.start()

window.mainloop()