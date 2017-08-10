import sys, json, os
import requests

def get_id(username):
	url="https://www.instagram.com/"+username+"/?__a=1"
	response = requests.get(url)
	respJSON = response.json()
	try:
		user_id = str(respJSON['user'].get("id"))
		return user_id
	except:
		print(respJSON)
		return "."

def main():

	if len(sys.argv) < 2:
		print("Usage: \npython main.py USERNAME")
		return

	user_id = get_id(sys.argv[1])

	print("ID: "+user_id)

if __name__ == "__main__":
    main()	