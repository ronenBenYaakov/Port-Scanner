import socket
import threading
from queue import Queue

target = 'IP address'
queue = Queue()
open_ports = []


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()

        if portscan(port):
            print("port" + port + "is open!")
        open_ports.append(port)


number_of_ports = 1024
port_list = range(1, number_of_ports)
fill_queue(port_list)

thread_list = []
number_of_threads = 100

for t in range(number_of_threads):
    thread = threading.Thread(target=worker())
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)
