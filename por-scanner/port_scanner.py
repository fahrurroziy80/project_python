import socket

def scan_port(target, port):
    print(f"Memindai {target} ....\n")
    for port in port:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((target, port))
            print(f"[OPEN] port {port}")
            s.close()
        except:
            pass

if __name__ == "__main__":
    target = input("Masukan alamat IP/host target: ")
    port = range(1, 1025)
    scan_port(target, port)