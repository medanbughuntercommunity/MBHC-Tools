import argparse
import socket
import time
import port_services

from datetime import datetime
from colorama import init, Fore
from threading import Thread, Lock
from queue import Queue

init()
RED = Fore.LIGHTRED_EX
YELLOW = Fore.LIGHTYELLOW_EX
GREEN = Fore.LIGHTGREEN_EX
BLUE = Fore.LIGHTBLUE_EX
WHITE = Fore.LIGHTWHITE_EX
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

N_THREADS = 200

PROG_VER = 0.3

q = Queue()
print_lock = Lock()

def port_scan(port):
    try:
        s = socket.socket()
        s.connect((host, port))
    except:
        with print_lock:
            print(f"{GRAY}[-] {host:15}:{port:5} is close {RESET}", end='\r')
    else:
        with print_lock:
            for element in port_services.services_array:
                try:
                    service = socket.getservbyport(port)
                    if element['portid'] == service:
                        print(f"{GREEN}[+] {host:15}:{port:5} [OPEN] --> {element['portdesc']} ({element['portid']}) {RESET}")
                        break
                except:
                    continue
            else:
                print(f"{GREEN}[+] {host:15}:{port:5} [OPEN] --> Unknown Service (unknown) {RESET}")
    finally:
        s.close()


def scan_thread():
    global q
    while True:
        worker = q.get()
        port_scan(worker)
        q.task_done()

def main(host, ports):
    start_time = time.time()
    print(f"{RED}########################################")
    print(f"##     __  __ ____  _    _  _____     ##")
    print(f"##    |  \/  |  _ \| |  | |/ ____|    ##")
    print(f"##    | \  / | |_) | |__| | |         ##")
    print(f"##    | |\/| |  _ <|  __  | |         ##")
    print(f"##    | |  | | |_) | |  | | |____     ##")
    print(f"##    |_|  |_|____/|_|  |_|\_____|    ##")
    print(f"##                                    ##")
    print(f"## Open Port Scanner                  ##")
    print(f"## Medan Bug Hunter Community         ##")
    print(f"##                                    ##")
    print(f"## By    : Deny Pradana               ##")
    print(f"## Email : dp@denypradana.com         ##")
    print(f"## Web   : https://denypradana.com    ##")
    print(f"########################################{RESET}")
    print(f"{WHITE}Program Version : {PROG_VER}{RESET}")
    print("")
    print(f"{YELLOW}Scan Started At {datetime.now().strftime('%H:%M:%S')} {datetime.now().strftime('%d-%m-%Y')}{RESET}")
    print("")
    print(f"{BLUE}RESULT : {RESET}")
    global q
    for t in range(N_THREADS):
        t = Thread(target=scan_thread)
        t.daemon = True
        t.start()

    for worker in ports:
        q.put(worker)
    
    q.join()
    
    print(f"{YELLOW}[=] Scan Finished At {datetime.now().strftime('%H:%M:%S')} {datetime.now().strftime('%d-%m-%Y')}. Total Time : {round(time.time() - start_time,1)} Seconds{RESET}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MBHC open port scanner")
    parser.add_argument("host", help="Host to scan.")
    parser.add_argument("--ports", "-p", dest="port_range", default="1-65535", help="Port range to scan, default is 1-65535 (all ports)")
    args = parser.parse_args()
    host, port_range = args.host, args.port_range

    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)

    ports = [ p for p in range(start_port, end_port)]

    main(host, ports)
