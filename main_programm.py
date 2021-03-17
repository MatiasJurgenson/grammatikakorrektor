from koostisosad import main_sonastik
from koostisosad import lause_leidja
from koostisosad import koma_main
from koostisosad import autocorrect_main



# vaja lisada kasutaja muudatus





#definitions
laused = []
lausenumber = 0

#"""_____"""#
#test lause = Ei sest, jah miks tud nud, aa o k.

while True:
    
    veakohad = []
    õigesti = []
    vea_arv = 0
    
    
    tekst = str(input("sisesta lause: "))
    laused = lause_leidja.lause_avaja(tekst)
    for lause in laused:
        for word in lause:
            wort = word.lower()
            sona = wort.replace(",", "") 
            if main_sonastik.oigekiri(sona) == None: # vaatab kas sõna on vale või õige
                print()
                print(str(sona) + " oli valesti kirjuatud")
                veakohad.append(sona)
                print(str(sona) + " soovitatud parandused: " + str(', '.join(map(str, autocorrect_main.autocorrect(sona)))))
                õigesti.append(autocorrect_main.autocorrect(sona))
                vea_arv += 1

        # komavea osa
        output = koma_main.komaviga(lause)
        asikoma = 1
        sama_vea_arv = 0
         
        
        for asi in output:
            if asikoma == 1:
                veakohad.extend(asi)
                asikoma = 2
            else:
                õigesti.extend(asi)
       

        for viga in veakohad:
            if veakohad[sama_vea_arv] == õigesti[sama_vea_arv]:
                õigesti.pop(sama_vea_arv)
                veakohad.pop(sama_vea_arv)
                sama_vea_arv += 1
            else:
                sama_vea_arv += 1
                    
        for viga in veakohad:
            if vea_arv < len(veakohad):
                print()
                print("vigane koht: " + '"' + str(veakohad[vea_arv]) + '"')
                print("õige vorm: " + '"' + str(õigesti[vea_arv]) + '"')
                vea_arv += 1

        lausenumber += 1
                
