import httplib2
from simplecrypt import decrypt

def load(userName="jeremy.martinez"):
	hashed_password = open('pass','r').read()

	hostName = "splunkes.wsu.edu"
	managementPort = "8089"
	userPassword = decrypt('password',hashed_password)
	testUri = "/services/apps/local"

	h = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
	h.add_credentials(userName, userPassword)

	base_url = "http://" + hostName + ":" + managementPort

	return base_url,testUri,h

def connect(base_url, testUri, h):
	try:
		response, content = h.request(base_url + testUri, "GET")
		if (response['status'] >= '200' and response['status'] <= '204'):
				return content
		else:
				return response['status']
	except Exception, e:
		print "Exception: '%s'" % e
		return None