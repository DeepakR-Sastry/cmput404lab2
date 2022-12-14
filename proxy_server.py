#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = "www.google.com"
PORT = 8001
BUFFER_SIZE = 1024

def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname(host)
    except:
        print("Hostname could not be resolved. Exiting")
        sys.exit()
    print(f'IP address of {host} is {remote_ip}')
    return remote_ip

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Starting proxy server")
        proxy_start.setsockopt(socket.SOL_SOCKET, socket_SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxt_start.listen(1)

        while True:
            conn, addr = proxt_start.accept()
            print("Connected by", addr)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print("Connecting to Google")
                remote_ip = get_remote_ip(host)
                proxy_end.connect((remote_ip, port))
                p = Process(target=handle_echo, args=(proxy_end, addr, conn))
                p.daemon = True
                p.start()
                print("Started Process ", p)
            conn.close()

def handle_echo(proxy_end, addr, conn):
    send_full_data = conn.recv(BUFFER_SIZE)
    print(f'Sending received data {send_full_data} to google')
    proxy_end.sendall(send_full_data)
    prox_end.shutdown(socket.SHUT_WR)
    data = proxy.end.recv(BUFFER_SIZE)
    print(f'Sending received data {data} to client')
    conn.send(data)

if __name__ == "__main__":
    main()
