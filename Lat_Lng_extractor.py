import requests

x = requests.get('http://localhost:8000/dataTable.txt')

twostr = (x.text).split('\n')[2:9]
i = 0
while i < len(twostr):
    dato =twostr[i].split(',')
    
    dati = dato[0].split(' ')
    dati2 = dato[1].split(' ')
    
    lat = dati[-1]
    lng = dati2[1]
    print(lat)
    print(lng)
    i+=1
