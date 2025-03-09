import socket
import threading

def port_scan(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        t.start()

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} on {target}: Open")
    except socket.error as e:
        print(f"Error on port {port}: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    targets = input("Enter the target IP addresses (comma-separated): ").split(',')
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    for target in targets:
        port_scan(target.strip(), start_port, end_port)