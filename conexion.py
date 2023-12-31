import socket
from Constanst import *
from algoritmo_de_minar import HashFinder


class Client:
    def __init__(self, host, port, user):
        self.host = host  # Server IP
        self.port = port  # Server port
        self.user = user  # User name
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            # Connect to the server
            self.socket.connect((self.host, self.port))
            print("Connected to server successfully!")
        except ConnectionRefusedError:
            print(
                "Connection refused. Please check if the server is running and the host and port are correct.")
        except Exception as e:
            print(f"An error occurred while connecting to the server: {e}")

    def send_user(self, msg=USER):
        self.socket.sendall(msg.encode())

    def send_message(self, message):
        message += '\n'  # Add a newline character to the end of the message
        message_bytes = message.encode('utf-8')
        self.socket.sendall(message_bytes)
        
    def receive_data(self):
        data = self.socket.recv(1024)
       
        return data.decode('utf-8')
    
    def close(self):
        self.socket.close()
