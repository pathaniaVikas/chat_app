import socket 
from utils import printl
from config_parser import config


user_name = socket.gethostname()


def receiver(ip, port):
    if type(port) is str:
        port = int(port)
        
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = (ip, port)
    printl('starting server on %s port %s: ' % server_addr)
    sock.bind(server_addr)

    sock.listen(1)
    while True:
        # wait for connection
        printl('waiting for connection ...')
        conn, client_addr = sock.accept()
        try:
            printl("got connection from ", client_addr)
            while True:
                data = conn.recv(1024)
                if len(data) > 0:
                    printl(str(user_name) + ' -> ' + data.decode('utf-8'))
        except Exception as e:
            printl(e)


if __name__ == '__main__':
    receiver(config['ADDRESS']['reciever_ip'], config['ADDRESS']['reciever_port'])