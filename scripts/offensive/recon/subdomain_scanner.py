import requests
import sys
# domain to scan supplied by user
domain = sys.argv[1]

# read a list of subdomains
subdomain_file = open("subdomains.txt").read() 
subdomain_list = subdomain_file.splitlines()

# empty list for discovered subdomains
discovered_domains = []

# iterate over list of subdomains
for subdomain in subdomain_list:
	req_url = f"http://{subdomain}.{domain}"

	try:
		# make a GET request with the url 
		requests.get(req_url)

	except requests.ConnectionError:
		# if the GET fails just move to the next item
		pass

	else:
		print("Subdomain discovered: ",req_url)
		# append the finding to the list
		discovered_domains.append(req_url)

# save the results to a file
with open("discovered_domains.txt", "w") as f:
	for subdomain in discovered_domains:
		print(subdomain,file=f)
