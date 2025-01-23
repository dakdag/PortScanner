import socket

def scan_ports(ip, start_port, end_port):
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)
        
        sock.close()
    
    return open_ports

def main():
    ip = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the start port number: "))
    end_port = int(input("Enter the end port number: "))
    
    print(f"Scanning IP address: {ip} from port {start_port} to {end_port}")
    
    open_ports = scan_ports(ip, start_port, end_port)
    
    if open_ports:
        print("\nOpen ports found:")
        for port in open_ports:
            print(f"Port {port} is OPEN")
    else:
        print("\nNo open ports found.")

if __name__ == "__main__":
    main()
