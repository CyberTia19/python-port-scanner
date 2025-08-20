# Python Port Scanner

A small, educational Python port scanner that checks a range of TCP ports on a target host.

# ⚠️ Use responsibly: Only scan devices you own or have explicit permission to test.

# ✨ Features

Interactive input or command-line arguments (--host, --start, --end)

Fast scanning with threading

No external dependencies (uses Python standard library)

# ⚙️ Requirements

Python 3.8 or higher

# 🚀 Usage
 * Interactive mode
python3 port_scanner.py


* You’ll be asked to enter the target host and port range.

 * Command-line arguments
python3 port_scanner.py --host 127.0.0.1 --start 1 --end 1024


Example output:

[+] Port 80 is open
[+] Port 443 is open
Scan complete.

# 📂 Project Structure
python-port-scanner/
│── LICENSE
│── README.md
│── .gitignore
│── port_scanner.py
|__ python-port-scanner

# 📝 License

This project is licensed under the MIT License – see the LICENSE file for details.
