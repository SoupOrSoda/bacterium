import configparser
import socket

print("Starting server!")

config = configparser.ConfigParser()
config.read('config.ini')

host = config['network']['host']
port = config['network']['port']

print("Server running on "+str(host)+":"+str(port))

# Nothing here yet!
