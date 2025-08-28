import argparse
from modules.portscan import port_scan
from modules.vulncheck import check_vulnerabilities

def main():
    parser = argparse.ArgumentParser(description="Chip Scan - Security Scanner")
    parser.add_argument("target", help="Target IP or hostname")
    args = parser.parse_args()

    print(f"🔎 Scanning target: {args.target}")
    
    # Step 1: Port Scan
    open_ports = port_scan(args.target)
    print(f"Open Ports: {open_ports}")

    # Step 2: Vulnerability Check
    if open_ports:
        print("\nChecking for vulnerabilities...")
        check_vulnerabilities(open_ports)
    else:
        print("No open ports detected.")

if __name__ == "__main__":
    main()
