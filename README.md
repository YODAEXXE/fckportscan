````md id="3f7n8v"
# ⚡ PyPort Scanner

A simple and fast multithreaded port scanner built with Python using `socket` and `threading`.

Perfect for learning:
- networking
- TCP/IP
- sockets
- multithreading
- cybersecurity

---

## 🚀 Features

- TCP Port Scanning
- Multithreading
- Fast scanning
- Configurable timeout
- Linux compatible
- Easy to modify

---

## 📸 Preview

```bash
[+] Port 22 open
[+] Port 80 open
[+] Port 443 open
````

---

## 🛠️ Technologies Used

* Python 3
* Socket
* Threading

---

## 📦 Installation

Clone the repository:

```bash id="70jlwm"
git clone https://github.com/yourusername/pyport-scanner.git
```

Enter the directory:

```bash id="jlwm8u"
cd pyport-scanner
```

---

## ▶️ Usage

```bash id="jlwm3n"
python scanner.py 192.168.0.1
```

Example:

```bash id="jlwm1p"
python scanner.py 192.168.0.10
```

---

## ⚠️ Disclaimer

This project was created for:

* educational purposes
* cybersecurity learning
* authorized lab environments

Do not use this tool on networks without permission.

---

## 🧠 How It Works

The scanner:

1. creates a TCP socket
2. attempts to connect to a port
3. analyzes the response
4. prints open ports

Threads allow multiple ports to be scanned simultaneously, making the scan much faster.

---

## 📂 Project Structure

```bash id="jlwm9v"
.
├── scanner.py
└── intro.py
```

---

## 🔥 Main Code

```python id="jlwm6q"
from intro import show_banner

show_banner(mode="glitch")

import socket
import threading
import sys

host = sys.argv[1]

threads = []

def scan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))

    if result == 0:
        print(f"[+] Port {port} open")

    sock.close()

for port in range(1, 1025):
    thread = threading.Thread(target=scan, args=(port,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
```

---

## 📌 Future Improvements

* Banner grabbing
* Service detection
* UDP scanning
* OS fingerprinting
* Export scan results
* GUI interface
* Advanced arguments

---

## 👨‍💻 Author

Samuel Morais

Project focused on networking and cybersecurity studies.

```
```
