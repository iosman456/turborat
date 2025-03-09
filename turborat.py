import socket

def port_scan(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    port_scan(target, start_port, end_port)