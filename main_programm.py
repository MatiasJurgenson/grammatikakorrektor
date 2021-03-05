from koostisosad import main_sonastik
from koostisosad import lause_leidja
from koostisosad import koma_main
from koostisosad import autocorrect_main

#definitions
laused = []

#"""_____"""#
#test lause = Ei sest, jah miks tud nud, aa o k.

lausenumber = 0
while True:
    tekst = str(input("sisesta lause: "))
    laused = lause_leidja.lause_avaja(tekst)
    print(laused)
    for lause in laused:
        for sona in lause:
            #print(main_sonastik.oigekiri(sona)) # test
            if main_sonastik.oigekiri(sona) == None: # vaatab kas sõna on vale või õige
                print()
                print(sona + " oli valesti kirjuatud")
                print(sona + " soovitatud parandused: " + str(', '.join(map(str, autocorrect_main.autocorrect(sona)))))
        if ' '.join(map(str, lause)) != ' '.join(map(str, koma_main.komaviga(lause))):
            print()
            viga_lause = laused[lausenumber]
            print("Leiti komaviga lauses: " + '"' + str(' '.join(map(str, viga_lause[0:-1])) + lause[-1]) + '"')
            print("parantatud lause variatsioon: " + str(' '.join(map(str, lause[0:-1])) + lause[-1]))
        lausenumber += 1
                

#lause leidja
#sonastik

#autocorrect
#teised pudipadi reeglid