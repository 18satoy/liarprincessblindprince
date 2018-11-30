#this is the file for the client for multiplayer aspect for now (Work in Progress)

import socket, os
import threading
from queue import Queue

HOST = "128.237.127.219"
PORT = 50004

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((HOST,PORT))
print("connected to server")
pid = os.getpid()

def handleServerMsg(server, serverMsg):
    server.setblocking(1)
    msg = ""
    command = ""
    while True:
        msg += server.recv(10).decode("UTF-8")
        command = msg.split("\n")
        while (len(command) > 1):
            readyMsg = command[0]
            msg = "\n".join(command[1:])
            serverMsg.put(readyMsg)
            command = msg.split("\n")

#above taken from sockets 112 manual

import pygame, random
from __init__ import *




serverMsg = Queue(100)
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()

play(serverMsg, server)
