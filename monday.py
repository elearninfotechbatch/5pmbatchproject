import json
import requests

res=requests.get('https://fakerapi.it/api/v1/books?_quantity=5')
books = res.json()
df= books['data']

for i in df[1:3]:
    print("Title:", i['title'])
    print("Title:", i['author'])
    print('---------------')


    
    


