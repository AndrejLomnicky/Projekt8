vstup=input("Zadaj mi retacez:")
pocetnost= dict()


for znak in vstup:
    if ord(znak)>=97 and ord(znak)<=122:
        if znak in pocetnost.keys():
            pocetnost[znak]+=1
        else:
            pocetnost[znak]=1
print(pocetnost)
