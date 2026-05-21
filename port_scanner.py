import socket

target = input("Enter target IP or domain: ")

print(f"\n[+] Scanning Target: {target}\n")

ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
    else:
        print(f"[CLOSED] Port {port}")

    s.close()
