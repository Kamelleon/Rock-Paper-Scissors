import random
import time
list=["kamien","papier","nozyce"]
while True:
    x=random.choice(list)
    y=str(input("""
        <------------------->
        |   WYBIERZ OPCJĘ:  |
        |                   |
        |     1. KAMIEN     |
        |     2. PAPIER     |
        |     3. NOZYCE     |
        |                   |
        <------------------->
        WYBRANA OPCJA: """))
    def gra():
        if ((x==list[2] and (y=="kamien" or y=="1" or y=="Kamien" or y=="Kamień" or y=="KAMIEN")) or (x==list[0] and (y=="papier" or y=="PAPIER" or y=="2" or y=="Papier")) or (x==list[1] and (y=="nozyce" or y=="Nożyce" or y=="3" or y=="NOZYCE"or y=="nożyce"))):
            print("""
        ---------------------
        |                   |
        |     WYGRAŁEŚ      |
        |                   |
        ---------------------""")
            print("Komputer wybrał: "+x)

        elif ((x==list[1] and (y=="kamien" or y=="1" or y=="Kamien" or y=="Kamień" or y=="KAMIEN")) or (x==list[2] and (y=="papier" or y=="PAPIER" or y=="2" or y=="Papier")) or (x==list[0] and (y=="nozyce" or y=="Nożyce" or y=="3" or y=="NOZYCE"or y=="nożyce"))):
            print("""
        ---------------------
        |                   |
        |     PRZEGRAŁEŚ    |
        |                   |
        ---------------------""")
            print("Komputer wybrał: "+x)

        elif ((x==list[0] and (y=="kamien" or y=="1" or y=="Kamien" or y=="Kamień" or y=="KAMIEN")) or (x==list[1] and (y=="papier" or y=="PAPIER" or y=="2" or y=="Papier")) or (x==list[2] and (y=="nozyce" or y=="Nożyce" or y=="3" or y=="NOZYCE" or y=="nożyce"))):
            print("""
        ---------------------
        |                   |
        |       REMIS       |
        |                   |
        ---------------------""")
            print("Komputer wybrał: "+x)

        else:
            print('!!! BRAK OPCJI !!!')

    gra()

    time.sleep(3)
