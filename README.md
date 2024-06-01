
# PyChitChat

A simple chat application to practice and learn networking.

## About

This chat application is built using Python's `socket` and `threading` libraries for networking, and `tkinter` for the graphical user interface (GUI). It consists of a server that handles multiple client connections and clients that can send and receive messages in real-time.

## Features

- Multi-client support
- Real-time messaging
- Graphical user interface (GUI) using Tkinter

## Requirements

- Python 3.x

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JMiller007/PyChitChat.git
   cd PyChitChat
   ```

2. **Ensure you have Python installed:**
   - Download and install Python from [python.org](https://www.python.org/).

## Running the Server

1. Open a terminal and navigate to the project directory.
2. Run the server script:
   ```bash
   python server.py
   ```

The server will start and listen for incoming connections on `127.0.0.1:12345`.

## Running the Client

1. Open another terminal and navigate to the project directory.
2. Run the client script:
   ```bash
   python client.py
   ```

A GUI window will open. You can type your messages in the entry box and click the "Send" button to send messages. The messages will appear in the scrollable text area.

## Testing the Application

1. **Start the Server:**
   - Ensure the server is running by following the steps in the "Running the Server" section.

2. **Connect Multiple Clients:**
   - Open multiple terminals or command prompts.
   - Run the client script in each terminal to open multiple client windows:
     ```bash
     python client.py
     ```

3. **Send and Receive Messages:**
   - Type messages in any client window and click "Send". The messages should appear in all connected client windows.

## Code Explanation

### Server (`server.py`)

The server code handles incoming client connections, receives messages from clients, and broadcasts those messages to all other connected clients. It uses `socket` for network communication and `threading` to handle multiple clients concurrently.

### Client (`client.py`)

The client code connects to the server, sends messages typed by the user, and displays messages received from the server. It uses `tkinter` to create a graphical user interface (GUI) for better user interaction.

- **`receive_messages` function:** Continuously listens for messages from the server and updates the GUI.
- **`send_messages` function:** Sends the user's message to the server and clears the entry box.
- **`start_client` function:** Initializes the client socket, sets up the GUI, and starts the threads for sending and receiving messages.

### Tkinter UI

The client GUI consists of:
- A scrollable text area to display messages.
- An entry box to type messages.
- A send button to send messages.

The `pack` geometry manager is used to arrange these widgets in the window.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
