import requests
def ability(name):
    url = "http://pokeapi.co/api/v2/pokemon/"+name+"/"
    payload=""
    response = requests.request("GET", url, data=payload)
    data = response.json()
    ality=[]
    for i in data["abilities"]:
        ality.append(i['ability']['name'])
    return ality