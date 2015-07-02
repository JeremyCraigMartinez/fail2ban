#!/usr/bin/python

from hash_pass import *
from search_splunk import *
from analyze_ip import *
import sys

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == "-p" or sys.argv[1] == "--password":
			hashed_password = create_password()
			write_password_to_file(hashed_password)

		if sys.argv[1] == "-h" or sys.argv[1] == "--help":
			print "enter -p or --password to enter initial password. Every subsequent invocation does not need -p/--password flag"
			exit()

	userName = "jeremy.martinez"
	#userName = input()

	base_url,testUri,h = load(userName)

	response = connect(base_url,testUri,h)

	if not response:
		pass
		#exit()
	elif isinstance(response, str):
		print response
		exit()
	
	#success
	json = ["134.121.1.1","43.32.45.5","69.166.42.2","69.165.3.3"]#= res_to_json(response)
	blacklisted_ips = compare(json)
	write_blacklisted_to_file(blacklisted_ips)