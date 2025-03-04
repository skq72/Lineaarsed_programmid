#Ülesanne 3
from math import *
from calendar import *
from datetime import *
from time import strptime

try:
    R=float(input("Sisesta R, kus R on ringi raadius:"))
    # ==, <, >, <=, >=
    if R<=0:
        print("Nulliga ja neg. arvudega ei ole mõtte töötada!")
    else:
        Ringi_S=round(pi*R**2)
        Ringi_P=round(2*pi*R)
        Ruudu_S=2*R*2*R
        Ruudu_P=4*2*R
        print(f"Ringi_S= {Ringi_S}\nRingi_P= {Ringi_P}\nRuudu_S= {Ruudu_S}\nRuudu_P= {Ruudu_P}")
except:
    print("Sisesta ainult arvud!!!")

    #Ülesanne 4
maa_R_km=6378
münte_d=22.75
maa_R_mm=maa_R_km*1000000
maa_p=2*pi*maa_R_mm
münte_arv=round(maa_p/münte_d)
print(f"On vaja {münte_arv} münte")

#Ülesanne 6
t="""
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
"""
print(t.upper())

#Ülesanne 5
a="kill-koll" .capitalize()
b="killadi-koll" .capitalize()
print(a, a, b, a, a, b, a, a, a, a)

#Ülesanne 7
a=float("Siseta ristküliku esimene külje pikkus:")
b=float("Siseta ristkülikuteine külje pikkus:")
ümbermõõt=2*(a+b)
pindala=a*b
print(f"Ristküliku ümbermõõt on {ümbermõõt} ja pindala on {pindala}")

#Ülesanne 8 
l=float("Siseta tangitud kütuse liitrid")
k=float("Siseta läbitud kilomeetrit")
try:
    if R<=0:
        print("Nulliga ja neg. arvudega ei ole mõtte töötada!")
    else:
        kesk_tarbimine=l/k*100
except:
    print("Sisesta ainult arvud!!!")

    #Ülesanne 9
    kiirus_kmh=29.9
    minutid=float(input("Siseta aeg rulluisutamisel:"))
    vahemaa_km=round({kiirus_kmh}/60*{minutid})
    print(f"rulluisutaja läbib {minutid} minutiga {vahemaa_kmh")


#Ülesanne 10
minutid_kas=int(input("Aeg minutides")
tunnid=minutid_kas//60
minutid=minutid_kas%60
print("vastus" .center(20, "*"))
