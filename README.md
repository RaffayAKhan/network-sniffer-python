# network-sniffer-python


## Overview
This project is a Python-based network sniffer and traffic analyzer built for educational purposes.  
It captures and analyzes TCP, UDP, and ICMP packets on the user’s own machine, providing insights into network traffic flow and protocol structure.

## Features
- Capture live packets from local network interface
- Parse IP, TCP, UDP, ICMP headers
- Display source/destination IPs and ports
- Optional filters by protocol or port
- Safe and ethical: no third-party network traffic is captured

## Requirements
- Python 3.11+
- Libraries:
  - `scapy`
  - `pandas` (optional, for analysis/logging)
  - `matplotlib` (optional, for visualization)
- Npcap installed on Windows

Install dependencies:
```bash
pip install -r requirements.txt
