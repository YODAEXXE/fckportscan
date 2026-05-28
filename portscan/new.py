from intro import show_banner

show_banner(mode="glitch")
import socket
import threading
import sys

host = sys.argv[1]

threads = []

def scan(porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((host, porta))
    if resultado == 0:
        print(f"[+] Porta {porta} aberta")
    sock.close()

for porta in range(1, 1025):
    thread = threading.Thread(target=scan, args=(porta,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join;()