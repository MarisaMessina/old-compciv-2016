import requests
resp = requests.get("https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-–-prepared-delivery-state-union-address/")
print (resp.status_code)
print (len(resp.text)) #this length is different than what's listed on our course website
print (resp.url)