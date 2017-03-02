print("Hello World")

f=open('0.html')
inp=f.read()
f.close()

print(len(inp))

import bs4

soup = bs4.BeautifulSoup(inp, "html.parser")

#print(soup.prettify())

import json
p = json.loads(inp)

print("\nFirst Message:")

print(p['actions'][0]['message_id'])
print(p['actions'][0]['timestamp_datetime'])
print(p['actions'][0]['author'])
print(p['actions'][0]['body'])

print("\nLast Message:")

num = -1
print(p['actions'][num]['message_id'])
print(p['actions'][num]['timestamp_datetime'])
print(p['actions'][num]['author'])
print(p['actions'][num]['body'])