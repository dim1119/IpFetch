import urllib.request
import json
def ipFetch():
	contents = urllib.request.urlopen("http://httpbin.org/ip").read()
	origin=json.loads(contents)['origin']
	ip= str(origin.split(',')[0])
	return ip

if __name__=='__main__':
	print("Your ip is "+ ipFetch())
