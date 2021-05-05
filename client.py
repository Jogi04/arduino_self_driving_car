import socket
import sys

from pynput.keyboard import Listener, Key

server_address = ('192.168.178.39', 80)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
print('Connected!')


def on_press(key):
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


def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
