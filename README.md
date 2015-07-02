##Fail2ban - WSU Network

This is a python script that is design to leverage the Splunk api [https://splunkes.wsu.edu/services/apps/local](https://splunkes.wsu.edu/services/apps/local)

This is implemented from a cron job via `cron.sh`. 

- Log file: debug.log
- Hashed password for api: pass
	- to initialize password, run `main.py --password` and type in your password when prompted (the file _pass_ will be created containing a hashed password). 
	- Then change permissions to this file so that only the user running the cron job can read `-r--------`

##Files explained

- `analyze_ip.py`
	- dependencies
		- `import ipaddress`
	- functions
		- `res_to_json(json)`: transform the response from splunk api into readable format `["999.999.999.999",...,"22.22.22.22"]` for script
		- `compare(malicious_ips)`: remove ip's from splunk response that are _whitelisted_ ip's
		- `write_blacklisted_to_file(malicious_ips)`: print malicious ip's to file for Ansible script to read
- `hash_pass.py`
	-dependencies
		- `from simplecrypt import encrypt`
		- `from getpass import getpass`
	- function
		- `create_password()`: prompt user for password (in plain text), and return encrypted password
		- `write_password_to(hashed_password)`: write hashed_password to the file `pass`
- `search_splunk`
	- dependencies
		- `import httplib2`
		- `import simplecrypt import decrypt`
	- functions
		- `load(userName="jeremy.martinez")`: assemble requirements (domain,paht,port,credentials,etc.) to connect to api
		- `connect(base_url, testUri, h)`: send request to api. Return response, status, or None
- `whitelist.json`
	- WSU ip networks
- `blacklist.json`
	- temporary file (array) of blacklisted ip's

##Main script explained

1. python ./main.py
	1. Check for command line arguments
		- `-h, --help` just tells user about --password options
		- `-p, --password` creates `pass` file
	2. loads _username_, and _pass_ for api call
	3. connects to api
		- terminate program if connection is unsuccessful
	4. convert response to readable format
	5. compare response to whitelisted ip's for ip's that we want to __actually__ block
	6. write ip's to `blacklist.json`
2. if `blacklist.json` is empty
	- __true__, print to `debug.log`: "nothing to blacklist"
	- __false__, invoke Ansible script

