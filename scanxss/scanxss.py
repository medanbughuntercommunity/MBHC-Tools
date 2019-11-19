#!/usr/bin/env python3
from core.colors import end, red, white, green, bad, good, info, run

try:
    import requests
except ImportError:
    import os
    print('%s requests isn\'t installed, installing now...' % info)
    os.system('pip3 install requests')
    print('%s requests has been installed, restart ScanXSS.' % info)
    quit()
try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    import os
    print('%s bs4 isn\'t installed, installing now...' % info)
    os.system('pip3 install bs4')
    print('%s bs4 has been installed, restart ScanXSS.' % info)
    quit()

import sys, getopt
from pprint import pprint
from urllib.parse import urljoin
from urllib.parse import urlparse

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
    print(f"%s Detected {len(forms)} forms on {url}." % run)
    inp = open("payloads.txt","r")
    for line in inp:
        js_script = line.strip()
        is_vulnerable = False
        
        for form in forms:
            form_details = get_form_details(form)
            content = submit_form(form_details, url, js_script).content.decode()
            if js_script in content:
                print(f"%s XSS Detected on {url}" % good)
                print(f"%s Form details:" % info)
                pprint(form_details)
                is_vulnerable = True
                
        return is_vulnerable
from urllib.parse import urlparse

def is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False

def main(argv):
    if not is_url(argv):
        print(f"%s Not a valid url !" % bad)
        print(f"%s Use standard url format. Example : http://{argv}.com, http://web.{argv}.com !" % bad)
        quit()

    print('%s##################################' % red)
    print('##  __  __ ____  _    _  _____  ##')
    print('## |  \/  |  _ \| |  | |/ ____| ##')
    print('## | \  / | |_) | |__| | |      ##')
    print('## | |\/| |  _ <|  __  | |      ##')
    print('## | |  | | |_) | |  | | |____  ##')
    print('## |_|  |_|____/|_|  |_|\_____| ##')
    print('##                              ##')
    print('## ScanXSS ver 0.2 beta         ##')
    print('## XSS Vulnerability Scanner    ##')
    print('##################################')
    print('%s' % end)
    print(scan_xss(argv))

if __name__ == "__main__":
    appname = sys.argv[0]
    try:
        main(sys.argv[1])
    except IndexError:
        print(f"%s Input Error !" % bad)
        print(f"%s Usage : python3 {appname} <target_url>" % bad)
        quit()