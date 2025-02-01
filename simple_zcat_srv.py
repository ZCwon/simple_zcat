import socket
import subprocess
import sys
import time
import threading
import asyncio
import io
import os

host = "0.0.0.0"    # Have the server listen on all interfaces
port = 7331     # listening on a non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a socket object, using IPv4 and TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow the port to be reused immediately after the server is killed
s.bind((host, port))     # Bind to the host and port that the server will listen on
s.listen(5)     # Enable the server to accept up to 5 concurrent connections
print(f"[*] Listening on {host}:{port}")

conn, addr = s.accept()     # Accept a connection from the client
print(f"[*] Connection from {addr[0]}:{addr[1]}")