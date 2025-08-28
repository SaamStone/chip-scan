# Mock vulnerability database
known_vulns = {
    21: "FTP service detected - check for anonymous login",
    22: "SSH open - ensure strong passwords/keys",
    3306: "MySQL exposed - check for weak credentials"
}

def check_vulnerabilities(open_ports):
    for port in open_ports:
        if port in known_vulns:
            print(f"[!] Port {port}: {known_vulns[port]}")
        else:
            print(f"[*] Port {port}: No known issues")
