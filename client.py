#!/usr/bin/python

import socket
import sys
from pynput.keyboard import Listener, Key


server_ip = ('192.168.178.39', 80)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_ip)
print('Connected!')


class KeyboardListener:
    def __init__(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()
            
    def on_press(self, key):
        if key == Key.esc:
            sys.exit()
        elif key.char == 'w':
            out_msg = 'w'
            client_socket.send(out_msg.encode())
        elif key.char == 's':
            out_msg = 's'
            client_socket.send(out_msg.encode())
        elif key.char == 'a':
            out_msg = 'a'
            client_socket.send(out_msg.encode())
        elif key.char == 'd':
            out_msg = 'd'
            client_socket.send(out_msg.encode())
        elif key.char == 'q':
            out_msg = 'q'
            client_socket.send(out_msg.encode())


if __name__ == '__main__':
    kb_listener = KeyboardListener()
