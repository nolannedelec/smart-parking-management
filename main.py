"""
Ce programme propose de générer une carte interactive dont la caractéristique principale est de présenter les taux de 
remplissage des parcs-relais de Rennes Métropole. Dans ce programme on utilise le formalisme JSON.
Auteurs: Nolan NEDELEC <nolan.nedelec29@gmail.com>
         Amandine KERLEROUX <amandine.kerleroux@isen-ouest.yncrea.fr>

"""

import requests
import folium
from datetime import datetime

def getDateElementsWithDatetime(dateSpring):

    # Convertir la chaîne de caractères en objet datetime
    date_obj = datetime.fromisoformat(dateSpring)
   
    print("Année:", date_obj.year)
    print("Mois:", date_obj.month)
    print("Jour:", date_obj.day)
    print("Heure:", date_obj.hour)
    print("Minute:", date_obj.minute)
    print("Seconde:", date_obj.second)
    titre=f'{date_obj.day}/{date_obj.month}/{date_obj.year} - {date_obj.hour+1}:{date_obj.minute}'
    return titre


def getColor(fillrate):
        if fillrate<50:
            couleur=('#00FF00')
        elif fillrate>50 and fillrate<80:
            couleur=('#FF8000')
        else:
            couleur=('#FF0000')
        return couleur

def getParkInformationWithJson(apiJSON):
    output=requests.get(apiJSON)
    dico_json=output.json()
    new_dico={}
    date=dico_json['results'][0]['lastupdate']
    for i in dico_json['results']:
        new_elem=[]
        nom=i['idparc']
        lat=i['coordonnees']['lat']
        lon=i['coordonnees']['lon']
        capamax=i['capacitesoliste']
        capaactuelle=i['jrdinfosoliste']
        new_elem.append(lat)
        new_elem.append(lon)
        new_elem.append(capamax)
        new_elem.append(capaactuelle)
        new_dico[nom]=new_elem
    return new_dico,date
           

def main():
    apiJSON='https://data.rennesmetropole.fr/api/explore/v2.1/catalog/datasets/tco-parcsrelais-star-etat-tr/records?limit=20'
    Informations,dateSpring=getParkInformationWithJson(apiJSON)

    # date pour le parking que l'on souhaite

    dateWithDatetime=getDateElementsWithDatetime(dateSpring)
   
    # couleurs pour chaque parking

    color_list=[]
    taux_fillrate_list=[]
    for i in Informations:
        capamax=int(Informations[i][2])
        capaoccupee=int(Informations[i][3])
        fillrate=(100*(capamax-capaoccupee))/capamax
        taux_fillrate_list.append(fillrate)
        get=getColor(fillrate)
        color_list.append(get)

    # folium/carte

    carte = folium.Map(location=(48.117266,-1.6777926),zoom_start=12)
    title_html = f'''
    <h3 align="center" style="font-size:20px"><b>{dateWithDatetime}</b></h3>
    '''
    carte.get_root().html.add_child(folium.Element(title_html))

    iteration=0
    for cle,valeur in Informations.items():
        folium.CircleMarker(location=[valeur[0],valeur[1]],color='Black',fill=True, fill_color='Black',fill_opacity=1, radius=10,
                            popup=str(cle)+'<br>'+'remplissage'+'<br>'+str(round(taux_fillrate_list[iteration]))+'%').add_to(carte)
        folium.CircleMarker(location=[valeur[0],valeur[1]],color=color_list[iteration],fill=True,fill_color=color_list[iteration],fill_opacity=1, 
                            radius=9*round(taux_fillrate_list[iteration])/100, 
                            popup=str(cle)+'<br>'+'remplissage'+'<br>'+str(round(taux_fillrate_list[iteration]))+'%').add_to(carte)
        iteration+=1

    carte.save('Map.Rennes.html')
main()