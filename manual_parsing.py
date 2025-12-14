"""
Ce programme propose de générer une carte interactive dont la caractéristique principale est de présenter les taux de 
remplissage des parcs-relais de Rennes Métropole. Dans ce programme on utilise les chaines de caractères.
Auteurs: Nolan NEDELEC <nolan.nedelec29@gmail.com>
         Amandine KERLEROUX <amandine.kerleroux@isen-ouest.yncrea.fr>

"""

import requests
import folium

def getDateElements(dateString):
    a=str(dateString)
    dico_temps={}
    e=''
    e=a[0]+a[1]+a[2]+a[3]
    dico_temps['année']=e
    e=a[5]+a[6]
    dico_temps['mois']=e
    e=a[8]+a[9]
    dico_temps['jour']=e
    e=a[11]+a[12]
    dico_temps['heure']=e
    e=a[13]+a[14]
    dico_temps['minute']=e
    chaine_temps=f'{dico_temps["jour"]}/{dico_temps["mois"]}/{dico_temps["année"]} - {int(dico_temps["heure"])+1}:{dico_temps["minute"]}'
    return dico_temps,chaine_temps

def getColor(fillrate):
        if fillrate<50:
            couleur=('#00FF00')
        elif fillrate>50 and fillrate<80:
            couleur=('#FF8000')
        else:
            couleur=('#FF0000')
        return couleur

def getParkInformation(apiString):
    output=requests.get(apiString)
    chaine=output.text
    chaine=chaine[30:]
    lst=[]
    v=0
    w=0
    for n,i in enumerate(chaine):
        if i=='{':
            if v==0:
                v=n
        elif i=='}':
            if w!=0:
                w=n
            else:
                w=1
        if v!=0 and w!=0 and w!=1:
            b=chaine[v:w+1]
            b=b.replace('{','')
            b=b.replace('}','')
            b=b.replace(':','')
            b=b.replace('[','')
            b=b.replace(']','')
            b=b.replace('"','')
            b=b.replace(',','')
            lst.append(b)
            v=0
            w=0
        new_list={}
        for o,j in enumerate(lst):
            liste_des_elements=j.split()
            new_elements=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
            nom=''
            for p,k in enumerate(liste_des_elements):
                if k=='idparc':
                    nom=liste_des_elements[p+1]
                if k=='etatouverture':
                    new_elements[0]=k
                    val=liste_des_elements[p+1]
                    new_elements[1]=val
                if k=='lastupdate':
                    new_elements[2]=k
                    val=liste_des_elements[p+1]
                    new_elements[3]=val
                if k=='lat':
                    new_elements[4]=k
                    val=liste_des_elements[p+1]
                    new_elements[5]=val
                if k=='lon':
                    new_elements[6]=k
                    val=liste_des_elements[p+1]
                    new_elements[7]=val
                if k=='capaciteparking':
                    new_elements[8]=k
                    val=liste_des_elements[p+1]
                    new_elements[9]=val
                if k=='capacitepmr':
                    new_elements[10]=k
                    val=liste_des_elements[p+1]
                    new_elements[11]=val
                if k=='jrdinfosoliste':
                    new_elements[12]=k
                    val=liste_des_elements[p+1]
                    new_elements[13]=val
                if k=='jrdinfopmr':
                    new_elements[14]=k
                    val=liste_des_elements[p+1]
                    new_elements[15]=val
            new_elements[16]='poccup'
            new_elements[17]=int(new_elements[9])-int(new_elements[13])
            new_elements[18]='poccuppmr'
            new_elements[19]=int(new_elements[11])-int(new_elements[15])

            new_list[nom]=new_elements
    return new_list

def main():
    apiString='https://data.rennesmetropole.fr/api/explore/v2.1/catalog/datasets/tco-parcsrelais-star-etat-tr/records?limit=20'
    Informations=getParkInformation(apiString)

    # date pour le parking que l'on souhaite

    dateinfo=Informations['JFK'][3]
    date,titre=getDateElements(dateinfo)

    # couleurs pour chaque parking
    color_list=[]
    taux_fillrate_list=[]
    for i in Informations:
        capamax=int(Informations[i][9])
        capaoccupee=int(Informations[i][13])
        fillrate=(100*(capamax-capaoccupee))/capamax
        taux_fillrate_list.append(fillrate)
        get=getColor(fillrate)
        color_list.append(get)

    # folium/carte

    carte = folium.Map(location=(48.117266,-1.6777926),zoom_start=12)
    iteration=0
    title_html = f'''
    <h3 align="center" style="font-size:20px"><b>{titre}</b></h3>
    '''
    carte.get_root().html.add_child(folium.Element(title_html))

    for cle,valeur in Informations.items():
        folium.CircleMarker(location=[valeur[5],valeur[7]],color='Black',fill=True,fill_color='Black',fill_opacity=1, radius=10, 
                            popup=str(cle)+'<br>'+'remplissage'+'<br>'+str(round(taux_fillrate_list[iteration]))+'%').add_to(carte)
        folium.CircleMarker(location=[valeur[5],valeur[7]],color=color_list[iteration],fill=True,
                            fill_color=color_list[iteration],fill_opacity=1, radius=9*round(taux_fillrate_list[iteration])/100, 
                            popup=str(cle)+'<br>'+'remplissage'+'<br>'+str(round(taux_fillrate_list[iteration]))+'%').add_to(carte)
        iteration+=1

    carte.save('Map.Rennes.html')
main()