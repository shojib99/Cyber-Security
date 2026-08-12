#!/usr/bin/env python3
import socket

host = input("Target host: ").strip()
n = int(input("How many ports to scan (from 1): ").strip())

print(f"\nScanning {host} ports 1..{n}...\n")

for port in range(1, n + 1):
    s = socket.socket()
    code = s.connect_ex((host, port))
    if code == 0:
        print(f"[OPEN] {port}")
    s.close()

print("\nScan finished.")
