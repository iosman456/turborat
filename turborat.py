import socket
import threading
import logging
from queue import Queue

# Logging configuration
logging.basicConfig(filename='scan_results.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thread lock for printing to avoid overlapping output
print_lock = threading.Lock()

def scan_port(target, port):
    """Scan a single port"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((target, port))
        with print_lock:
            if result == 0:
                print(f"Port {port} on {target}: Open")
                logging.info(f"Port {port} on {target}: Open")
            else:
                logging.info(f"Port {port} on {target}: Closed")
    except socket.error as e:
        with print_lock:
            print(f"Error on port {port}: {e}")
            logging.error(f"Error on port {port}: {e}")
    finally:
        sock.close()

def threader(queue):
    while True:
        worker = queue.get()
        scan_port(worker[0], worker[1])
        queue.task_done()

def port_scan(target, start_port, end_port, thread_count):
    """Scan a range of ports on a target IP address"""
    print(f"Scanning {target} from port {start_port} to {end_port} with {thread_count} threads")
    queue = Queue()
    
    for _ in range(thread_count):
        thread = threading.Thread(target=threader, args=(queue,))
        thread.daemon = True
        thread.start()
    
    for port in range(start_port, end_port + 1):
        queue.put((target, port))
    
    queue.join()

def main():
    # Kullanıcının inputlarını al
    target = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port number: "))
    end_port = int(input("Enter the end port number: "))
    thread_count = int(input("Enter the number of threads (default: 10): ") or 10)

    port_scan(target, start_port, end_port, thread_count)

if __name__ == "__main__":
    main()