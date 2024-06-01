import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to connect to

def receive_messages(client_socket, text_area):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                text_area.config(state=tk.NORMAL)
                text_area.insert(tk.END, message + '\n')
                text_area.config(state=tk.DISABLED)
                text_area.see(tk.END)
            else:
                break
        except:
            break

def send_messages(client_socket, message_entry):
    message = message_entry.get()
    client_socket.send(message.encode('utf-8'))
    message_entry.delete(0, tk.END)

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"Connected to chat server on {HOST}:{PORT}")

    # Tkinter UI setup
    root = tk.Tk()
    root.title("PyChitChat")

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    message_entry = tk.Entry(root, width=50)
    message_entry.pack(padx=10, pady=5, side=tk.LEFT, fill=tk.X, expand=True)

    send_button = tk.Button(root, text="Send", command=lambda: send_messages(client_socket, message_entry))
    send_button.pack(padx=10, pady=5, side=tk.RIGHT)

    threading.Thread(target=receive_messages, args=(client_socket, text_area)).start()

    root.mainloop()

if __name__ == "__main__":
    start_client()
