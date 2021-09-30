from multiprocessing import Pool
import requests
import sys

# USAGE EXAMPLE: python3 dir_scanner.py <wordlist> <target address> <file extension>

discovered_dirs = []
# read in the wordlist
dir_file = open(f"{sys.argv[1]}").read() 
dir_list = dir_file.splitlines()

def make_request(dir_list):
        # create a GET request URL base on items in the wordlist
        req_url = f"http://{sys.argv[2]}/{dir_list}.{sys.argv[3]}"
        return req_url, requests.get(req_url)
# map the requests made by make_requests to speed things up
with Pool(processes=4) as pool:
    for req_url, req_dir in pool.map(make_request, dir_list):
        # if the request resp is a 404 move on
        if req_dir.status_code == 404:
            pass
        # if not a 404 resp then add it to the list
        else:
            print("Directroy Discovered ", req_url)
            discovered_dirs.append(req_url)
    # create a new file and append it with directories that were discovered
    with open("discovered_dirs.txt","w") as f:
        for directories in discovered_dirs:
            print(req_url,file=f)
