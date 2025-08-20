import socket
import argparse

def scan_ports(host, start_port, end_port):
    print(f"\n[+] Scanning {host} ports {start_port}-{end_port}...\n")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    print("\n[+] Scan complete.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("--host", required=True, help="Target IP address or hostname")
    parser.add_argument("--start", type=int, required=True, help="Start port number")
    parser.add_argument("--end", type=int, required=True, help="End port number")
    args = parser.parse_args()

    scan_ports(args.host, args.start, args.end)
