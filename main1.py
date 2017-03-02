print("Hello, World!")

import requests

#<USER_ID>?access_token=PAGE_ACCESS_TOKEN.

page = "https://graph.facebook.com/v2.8/"
usrid = "100008183341012"
fields = "?fields=first_name,last_name,profile_pic,locale,timezone,gender"

print("this is working")



quit()

#CHECK PERMISSIONS
token = page + usrid + "/permissions"
u = requests.get(token)
print(u)
print(u.content)

quit()

#LOGIN
print("LOGGING IN")
token = page + "oauth/access_token?" + "client_id=1245225482240854" + "&client_secret=1bb16950ea61f5ce10c73c11e4d4019d" + "&grant_type=client_credentials"
u = requests.get(token)
print(u)
print(u.content)
print("LOGIN COMPLETE\n")
access_token = "&access_token=" + u.content[0]

#GET INFO
'''
print("GETTING INFO")
token = page + usrid + fields + access_token
u = requests.get(token)
print(u)
print(u.content)
'''

#GET INBOX
token = page + usrid + "/inbox"
u = requests.get(token)
print(u)
print(u.content)

#token = page + usrid + "/inbox"

#u = requests.get(token)
#print(u)
#print(u.content)
# 100008183341012