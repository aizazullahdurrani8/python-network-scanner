#!/usr/bin/env python3
import scapy.all as scapy
import argparse
import sys

# Show message if no arguments are passed
if len(sys.argv) == 1:
    print("[-] Please provide arguments. Use --help for usage.")
    exit(1)

# Function to parse command-line arguments
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP address/IP range", required=True)
    return parser.parse_args()

# Function to perform ARP scan on the target IP/range
def scan(ip):
    # Create an ARP request packet
    arp_request = scapy.ARP(pdst=ip)

    # Create an Ethernet frame to broadcast the ARP request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combine the Ethernet frame and ARP request into a single packet
    arp_request_broadcast = broadcast / arp_request

    # Send the packet and receive responses
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # Store the IP and MAC addresses of responding devices
    clients_list = []
    for answer in answered:
        client = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}
        clients_list.append(client)

    return clients_list

# Function to display the scan results
def print_results(results):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in results:
        print(f"{client['ip']}\t\t{client['mac']}")

# Get the target IP range from user input
options = get_arguments()

# Perform the scan and display results
scan_results = scan(options.target)
print_results(scan_results)