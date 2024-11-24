import httplib, urllib
params = urllib.urlencode({'number': 12524, 'type': 'issue', 'action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"}
conn = httplib.HTTPConnection("bugs.python.org")
conn.request("POST", "", params, headers)
response = conn.getresponse()
print response.status, response.reason
302 Found
data = response.read()
data
'Redirecting to <a href="http://bugs.python.org/issue12524">http://bugs.python.org/issue12524</a>'
conn.close()
