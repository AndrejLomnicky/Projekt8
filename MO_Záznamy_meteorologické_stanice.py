#relativna cesta ide z pythonu do súboru txt. Špeciálny znak: ../../jozo
fr = open("subory/meteo_stanice.txt","r",encoding="utf-8")#r-znamená read
pocitadlo = 0
teploty=[]
for row in fr:
    processed_line = row.strip().split(" ")
    teploty.append(processed_line[3].replace( ",","."))#vyber tretiu hodnotu z processed line a drbni ju do teploty #vymenili sme čiarky na bodky
    print(processed_line)
    pocitadlo += 1
print(f"Pocet merani je {pocitadlo}")
print(f"Teploty sú {teploty}")
print(f"najvyssia teplota je {max(teploty)}")








