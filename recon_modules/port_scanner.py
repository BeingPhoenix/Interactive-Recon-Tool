# recon_modules/port_scanner.py
def port_scanner(target, start_port, end_port, threads):
    import socket
    import threading

    def scan_port(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((ip, port))
            print(f"[+] Found open port: {port}")
        except (socket.timeout, ConnectionRefusedError):
            pass
        finally:
            s.close()

    print(f"[+] Scanning target {target} from port {start_port} to {end_port} using {threads} threads")
    for port in range(start_port, end_port + 1):
        while threading.active_count() > threads:
            pass
        t = threading.Thread(target=scan_port, args=(target, port))
        t.start()

