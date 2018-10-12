import requests, json, re

number = []

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.8',
    'Cache-Control':'max-age=0',
    'Content-Type':'application/x-www-form-urlencoded',
    'Host':'www.partsgateway.co.uk',
    'Origin':'http://www.partsgateway.co.uk',
    'Referer':'http://www.partsgateway.co.uk',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

plate = ""

plate = input("Enter your plate : ")
print("Searching for Plate " + plate)


# Here is the form data
data = {
    'vrm': plate
}

url = "https://www.partsgateway.co.uk/parts/enquiry"
response = requests.post(url, data=data, headers=headers)

try:
	data = re.search("vehicle =\s+({.+})", response.text).group(1)
except AttributeError:
	print('Couldn\'t find vehicle data!')
	exit()

data = json.loads(data)

print(json.dumps(data, indent=2, sort_keys=True))
