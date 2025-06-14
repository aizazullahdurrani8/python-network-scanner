# ARP Network Scanner

This script allows you to scan a target IP address or IP range to discover live devices on the network by sending ARP requests and collecting their IP and MAC addresses.

## Getting Started

To get a copy of this project up and running on your local machine, follow these steps.

### Prerequisites

- Python 3 installed on your system.
- `scapy` Python library installed (`pip install scapy`).
- Appropriate permissions to send network packets (usually requires running as root or with sudo on Linux).

### Cloning the Repository

You can clone this repository using HTTPS:

    git clone https://github.com/aizazullahdurrani8/python-network-scanner.git

## Usage

Navigate into the cloned directory and run the script with the required arguments.

### Arguments

- `-t` or `--target`: Specify the target IP address or IP range (e.g., `192.168.1.1` or `192.168.1.0/24`).

### Example

To scan the entire subnet `192.168.1.0/24`:

    sudo python3 network_scanner.py -t 192.168.1.0/24

To scan a single IP address `192.168.1.105`:

    sudo python3 network_scanner.py -t 192.168.1.105

## How it Works

The script performs the following actions:

1. **Takes Command-Line Arguments**: Uses `argparse` to get the target IP address or range.

2. **Sends ARP Requests**:

   - Creates an ARP request packet for the specified target(s).
   - Broadcasts the request on the network.
   - Waits for responses from live devices.

3. **Collects Responses**: Parses the responses to retrieve IP and MAC addresses.

4. **Displays Results**: Prints a formatted list of all discovered devices with their IP and MAC addresses.

## Disclaimer

This tool is for educational purposes only. Scanning networks without permission may be illegal or violate network policies. Always ensure you have authorization before performing network scans.
