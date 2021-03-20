import socket
from utils import printl
from config_parser import config


def sender(ip, port):
    if type(port) is str:
        port = int(port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    printl('connecting to %s port %s' % server_address)
    sock.connect(server_address)
    while True:
        try:
                # Send data
            message = input()
            msg = bytes(message, 'utf-8')
            sock.sendall(msg)
        except Exception as e:
            printl(e)


if __name__ == '__main__':
    sender(config['ADDRESS']['reciever_ip'], config['ADDRESS']['reciever_port'])