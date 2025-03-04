from math import sqrt
from math import *
from math import pi

# #---------
# print("Ruudu karakteristikud")
# try:
#     a=int(input('Sisesta ruudu külje pikkus => '))
#     if a>0:
#         S=a**2
#         print(f"Ruudu pindala, {S}")
#         P=4*a
#         print(f"Ruudu ümbermõõt {P}")
#         di=a*sqrt(2)
#         print("Ruudu diagonaal", round(di,2))
#     else:
#         print("Külg ei saa olla <=0-ga")
# except:
#     print("Külje suurus on vaja int formaadis sisestada!!")
# #---------


# print("Ristküliku karakteristikud")
# try:
#     b=int(input("Sisesta ristküliku 1. külje pikkus => "))
#     c=int(input("Sisesta ristküliku 2. külje pikkus => "))
#     if b>0 and c>0:
#         S=b*c
#         print(f"Ristküliku pindala, {S}")
#         P=2(b+c)
#         print(f"Ristküliku ümbermõõt {P}")
#         di=sqrt(b*2+c*2)
#     else:
#         print("Ristküliku diagonaal", round(di))
# except:
#         print("Risküliku 1. või 2. on vaja int formaadis sisestada!!!")
#---------



print("Ringi karakteristikud")
try:
    r=int(input("Sisesta ringi raadiusi pikkus =>"))
    if r>0:
        d=2*r
        print(f"Ringi läbimõõt", d)
        S=pi*r*2
        print("Ringi pindala", round(S))
        C=2*pi*r
        print("ringoone pikkus", round(C))
    else:
       print("Külg ei saa olla <=0-ga")
except:
    print("Ringi raadius on vaja int formaadis sisestada!!!")
#-----------