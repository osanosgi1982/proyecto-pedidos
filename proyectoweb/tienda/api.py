# import requests
# url="https://pokeapi.co/api/v2/pokemon"

# response=requests.get(url)


# for pokemon in response.json()['results']:
#     print(pokemon["name"])

#---------------------------------------------
# import json
# import requests
# url="https://api.jikan.moe/v4/top/anime"
# data=requests.get(url)
# if data.status_code==200:
#     data=data.json()
#     for e in data['data']:
#         print(e["title"]," ",e["type"])

#------------------------------------------

from urllib.request import urlopen
import json

url="https://random-data-api.com/api/commerce/random_commerce?size=100"
response = urlopen(url)
#print(response.read())
data= json.load(response)
diccionario={}
j=0
for i in data:
    if i["material"] not in diccionario.values():
        diccionario[j]=i["material"]
        j+=1
print(diccionario)


