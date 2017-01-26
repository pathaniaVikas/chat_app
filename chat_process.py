import socket 
import sys
import _thread
import threading

listener_ip = 'localhost'
sending_to_ip = 'localhost'
receiver_port = 10234
Lock = threading.Lock()

user_name = socket.gethostname()

def printl(*data):
    with Lock:
        final_string = ''
        for d in data:
            final_string = final_string + str(d)
        print(final_string)
    
def receiver(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = (ip, port)
    printl('starting server on %s port %s: ' % server_addr)
    sock.bind(server_addr)

    sock.listen(1)
    while  True:
        #wait for connection
        printl('waiting for connection ...')
        conn, client_addr = sock.accept()
        try:
            printl("got connection from ", client_addr)
            while True:
                data = conn.recv(1024)
                if len(data)>0:
                    printl(str(user_name) + ' -> ' + data.decode('utf-8'))
        except Exception as e:
            printl(e)

def sender(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    printl('connecting to %s port %s' % server_address)
    sock.connect(server_address)
    while True:
        try:    
                # Send data
            message = input()
            msg= bytes(message, 'utf-8')
            sock.sendall(msg)
        except Exception as e:
            printl(e)

if __name__ == '__main__':

    server_addr = (listener_ip, receiver_port,)
    _thread.start_new_thread(receiver, server_addr)
    import time
    time.sleep(2)
    sender(sending_to_ip, receiver_port)