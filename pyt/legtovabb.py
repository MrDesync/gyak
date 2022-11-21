import eauto
autok = []
for i in range(3):
    nev=input('Adja meg az elektromos autó nevét!')
    km=int(input('Hány km-t tud megtenni egy feltöltéssel?'))
    autok.append(eauto.Eauto(nev,km))
legtovabb = autok[0]
for auto in autok:
    print(f"A(z) {auto.nev} {auto.km} km-t tuf megtenni egy feltöltéssel")
    if legtovabb.km < auto.km:
        legtovabb = auto
with open("legtovabb.txt", "w", encoding="utf-8") as f:
    f.write(legtovabb.nev)