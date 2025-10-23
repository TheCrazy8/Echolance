#!/usr/bin/env python3
"""
Helper script to display network information for WebPyChat
"""
import socket
import sys

def get_local_ip():
    """Get the local IP address of this machine"""
    try:
        # Create a socket to determine the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "Unable to determine"

def main():
    print("=" * 60)
    print("WebPyChat Network Information")
    print("=" * 60)
    print()
    
    hostname = socket.gethostname()
    local_ip = get_local_ip()
    
    print(f"Hostname:     {hostname}")
    print(f"Local IP:     {local_ip}")
    print()
    print("Access URLs:")
    print(f"  Local:      http://localhost:5000")
    print(f"  Network:    http://{local_ip}:5000")
    print()
    print("Share the Network URL with others on your local network")
    print("to allow them to join the chat!")
    print("=" * 60)

if __name__ == '__main__':
    main()
