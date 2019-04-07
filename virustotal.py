import requests, sys,json
import hashlib
import io


# assigns the values passed in at the command line to variables
user_api_key = None 
file = None

def filepath(file):
	if file == None:
		src = input('File Path: ')
	else:
		src = file
	return src

noescfile = filepath(file)
dahfile = os.path.join(noescfile).replace(" ", "\\ ")

def apikey(user_api_key):
	if user_api_key == None:
		apii = input(' Api Key?: ')
	else:
		apii = user_api_key
	return apii
api = apikey(user_api_key)

def gethash(dahfile, length=io.DEFAULT_BUFFER_SIZE):
	md5 = hashlib.md5()
	with io.open(dahfile, mode="rb") as fd:
		for chunk in iter(lambda: fd.read(length), b''):
			md5.update(chunk)
	return md5
hashh = gethash(dahfile, length=io.DEFAULT_BUFFER_SIZE)

params = {
    'apikey': api,
    'resource': hashh
    }


# makes json pretty
def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
        return None

if __name__ == '__main__':
	response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
	json_response = response.json()
	pretty_json = pp_json(json_response)
	print(pretty_json)