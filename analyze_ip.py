import ipaddress

def res_to_json(json):
	return None
	# transform content into JSON

import json
def compare(malicious_ips):
	white_listed_ips_raw = open('whitelist.json','r').read()

	white_listed_ips = json.loads(white_listed_ips_raw)
	white_listed_ips = white_listed_ips['all']

	for ip in malicious_ips:
		for w_ip_network in white_listed_ips:
			if ipaddress.ip_address(unicode(ip)) in ipaddress.ip_network(unicode(w_ip_network)):
				malicious_ips = malicious_ips[:malicious_ips.index(ip)]+malicious_ips[malicious_ips.index(ip)+1:]
	return malicious_ips

def write_blacklisted_to_file(malicious_ips):
	with open('blacklist.json','w') as f:
		f.write("%s%s%s"%("[\"","\",\"".join(malicious_ips),"\"]"))