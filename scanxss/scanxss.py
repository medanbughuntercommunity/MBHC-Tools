import sys
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from colorama import init, Fore

init()
RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def scan_xss(url):
    forms = get_all_forms(url)
    print(f"{BLUE}[+] Detected {len(forms)} forms on {url}. {RESET}")
    inp = open("payloads.txt","r")
    for line in inp:
        js_script = line.strip()
        is_vulnerable = False
        
        for form in forms:
            form_details = get_form_details(form)
            content = submit_form(form_details, url, js_script).content.decode()
            if js_script in content:
                print(f"{GREEN}[+] XSS Detected on {url} {RESET}")
                print(f"[*] Form details:")
                pprint(form_details)
                is_vulnerable = True
                
        return is_vulnerable

if __name__ == "__main__":

    url = sys.argv[1]
    print(f"{RED}##################################")
    print(f"##  __  __ ____  _    _  _____  ##")
    print(f"## |  \/  |  _ \| |  | |/ ____| ##")
    print(f"## | \  / | |_) | |__| | |      ##")
    print(f"## | |\/| |  _ <|  __  | |      ##")
    print(f"## | |  | | |_) | |  | | |____  ##")
    print(f"## |_|  |_|____/|_|  |_|\_____| ##")
    print(f"##                              ##")
    print(f"## XSS Scanner ver 0.1 beta     ##")
    print(f"################################## {RESET}")
    print(scan_xss(url))