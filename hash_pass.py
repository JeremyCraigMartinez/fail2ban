from simplecrypt import encrypt
from getpass import getpass

def create_password():
	master_secret_key = getpass()
	return encrypt('password', master_secret_key)

def write_password_to_file(hashed_password):
	with open('pass','w') as f:
		f.write(hashed_password)