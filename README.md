# 🔎 Chip Scan  

A lightweight **port & vulnerability scanner** built in Python.  
Chip Scan helps security enthusiasts and students perform **basic reconnaissance** by scanning hosts for open ports and checking for common vulnerabilities.

---

## 🚀 Features
- ✅ Scan for open ports on a target host/IP  
- ✅ Basic vulnerability detection (mock database for known issues)  
- ✅ Simple CLI usage with `argparse`  
- ✅ Modular design (`portscan.py`, `vulncheck.py`)  
- ✅ Lightweight & portable (no heavy dependencies)  

---

## 📂 Project Structure
chip-scan/
│── chipscan.py # Main script (entry point)
│── modules/
│ ├── portscan.py # Handles port scanning
│ ├── vulncheck.py # Handles vulnerability checks
│── requirements.txt # Dependencies (minimal)
│── README.md # Project documentation


---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/SaamStone/chip-scan.git
cd chip-scan


(Optional) Create a virtual environment

python -m venv venv
venv\Scripts\activate    # On Windows
# or
source venv/bin/activate # On Linux/Mac


Install dependencies

pip install -r requirements.txt

🖥️ Usage
# General help
python chipscan.py -h

# Scan localhost
python chipscan.py 127.0.0.1

# Scan a website
python chipscan.py scanme.nmap.org


📌 Example Output:

🔎 Scanning target: 127.0.0.1
Open Ports: [22, 80]

Checking for vulnerabilities...
[!] Port 22: SSH open - ensure strong passwords/keys
[*] Port 80: No known issues

🔮 Future Improvements

Integrate real CVE lookups via Vulners API

Add multi-threaded scanning for faster results

Include IoT / Chip-specific vulnerability checks

Export results in JSON/HTML format

📜 License

This project is for educational purposes only.
Do not use it on networks without proper authorization.

👨‍💻 Author: Sairam (SaamStone)
🚀 Built with Python & a passion for Cybersecurity
