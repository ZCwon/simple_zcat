import argparse
import socket
import subprocess
import sys
import threading
import os
import time
from win32com.shell import shell, shellcon # Import the required modules for the Windows version of the script

host = "127.0.0.1" # Change this to the server address, set to loopback for local testing
port = 7331 # Change this to the port the server is listening on

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a new socket object using IPv4 and TCP
try:
    client.connect((host, port)) # Connect to the server
except:
    print("Error connecting, check the host and port")
    os._exit(0)