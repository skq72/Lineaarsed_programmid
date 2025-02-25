from random import * #importeerimine 
from math import *
#Ülesanne 1
nimi=input("Mis on sinu nimi?: ")
vanus=int(input("Kui vana sa oled?: "))
pikkus=int(input("Kui pikk sa oled?: "))

print(f"Tere, maailm! Tervitan sind {nimi} Sa oled {vanus} aastat vana.")
print("Tere, maailm! Tervitan sind",nimi,"Sa oled",vanus,"aastat vana.")
print("Tere, maailm! Tervitan sind"+nimi+"\nSa oled"+str(vanus)+"aastat vana.")

#Ülesanne 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis= True
print(f"Muutuja {vanus} on {type(vanus)} tüübi")
print(f"Muutuja {eesnimi} on {type(eesnimi)} tüübi")
print(f"Muutuja {pikkus} on {type(pikkus)} tüübi")
print(f"Muutuja {kas_käib_koolis} on {type(kas_käib_koolis)} tüübi")

#Ülesanne 3
kommidearv=randint(1,100)
print(f"Laual on {kommidearv} kommid")
kommidvõtmud=int(input("Mittu kommid tahad ära võtta?"))
onjäänud=kommidearv-kommidvõtmud
print(f"Laual on jäänud {onjäänud} kommid")

#Ülesanne 4
ümbermõõt=int(input("Kui suur on ümbermõõt?: "))
läbimõõt=ümbermõõt//pi
print(f"läbimõõt on {läbimõõt}")
