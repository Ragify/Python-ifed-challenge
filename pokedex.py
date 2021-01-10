import PySimpleGUI as sg
import requests


layout = [[sg.Text("Enter the name of Pokemon:")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(100,1), key='-OUTPUT1-')],
          [sg.Text(size=(100,1), key='-OUTPUT2-')],
          [sg.Text(size=(100,3), key='-OUTPUT3-')],
          [sg.Text(size=(100,15), key='-OUTPUT4-')],
          [sg.Text(size=(100,1), key='-OUTPUT5-')],
          [sg.Button('Search'), sg.Button('Quit')]]

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
    


window = sg.Window('PokeDex', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    Details="Name of the pokemon:"+values['-INPUT-']
    window['-OUTPUT1-'].update(Details) 
    name=values["-INPUT-"]

    #TYPE OF POKEMON

    urll = "http://pokeapi.co/api/v2/pokemon/"+name+"/"
    urls=[]
    tp=[]
    data = requests.get(urll).json()
    for i in range (2):
        poke_type=data["types"][i]['type']['name']
        urls.append(data["types"][i]['type']['url'])
        tp.append(poke_type)

    Details="Type of pokemon is: "+str(tp)
    window['-OUTPUT2-'].update(Details)
    
    #DOUBLE DAMAGE FROM
    
    Details="Double Damage from: \n"
    d_dmg_url=[]
    cn=0
    tpp=tp
    tp=[]
    for url in urls:
        poke_type=requests.get(url).json()
        Details+="Double Damage for "+tpp[cn]+" by: "
        cn+=1
        for j in poke_type["damage_relations"]["double_damage_from"]:
            Details+=j["name"]+' '
            tp.append(j["name"])
            d_dmg_url.append(j["url"])
        Details+='\n'
    window['-OUTPUT3-'].update(Details)
    
    #LISTING 5 POKEMON

    Details='The 5 pokemons which gives the given pokemon double damage:\n'
    print(d_dmg_url)
    for i in range(len(d_dmg_url)):
        dat=requests.get(d_dmg_url[i]).json()
        Details+=("Pokemon of Type: "+tp[i]+'\n')
        for j in range(5):
            Details+=(dat["pokemon"][j]["pokemon"]["name"])
            if j!=4:
                Details+=(',')
        Details+=("\n\n")
    
    window['-OUTPUT4-'].update(Details)

    #ABILITY

    Details="Ability: "+str(ability(values['-INPUT-']))
    window['-OUTPUT5-'].update(Details)

window.close()