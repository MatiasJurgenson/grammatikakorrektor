fail = open("lemmad2013.txt", encoding = "UTF-8")
for rida in fail:
    sisu = fail.read()
    sonastik = sisu.splitlines()

fail.close()

#seda läheb vaja järgmises def-is
def it(protsendid, pot_oige, sobilikud_sonad):
    for i in range (len(protsendid)):        
        if protsendid[i] == max(protsendid):
            pot_oige.append(sobilikud_sonad[i])
            protsendid.pop(i)
            sobilikud_sonad.pop(i)
            return (pot_oige, sobilikud_sonad)

def autocorrect(x):
    protsendid = []
    sobilikud_sonad = []
    valesona = list(x)
    valesona_pikkus = len(valesona)
    for sona in sonastik:
        if len(sona) < (valesona_pikkus + 2) and len(sona) > (valesona_pikkus - 2) and sona[0] == valesona[0]: 
            sobilikud_sonad.append(sona)
            valesona_tahejarg = 0
            sona_tahejarg = 0
            oigete_tahtede_arv = 0
            
            #kui valesona on suurem  
            if len(valesona) > len(sona):
                for taht in valesona:
                    if valesona_tahejarg < valesona_pikkus and sona_tahejarg < len(sona):
                        if valesona[valesona_tahejarg] == sona[sona_tahejarg]:
                            oigete_tahtede_arv += 1
                            valesona_tahejarg += 1
                            sona_tahejarg += 1
                        elif valesona[valesona_tahejarg] != sona[sona_tahejarg]:
                            valesona_tahejarg += 1
                protsendid.append(round(oigete_tahtede_arv/len(sona)*100))
                
            #kui valesona on väiksem     
            elif len(valesona) < len(sona):
                for taht in sona:
                    if valesona_tahejarg < valesona_pikkus and sona_tahejarg < len(sona):
                        if valesona[valesona_tahejarg] == sona[sona_tahejarg]:
                            oigete_tahtede_arv += 1
                            valesona_tahejarg += 1
                            sona_tahejarg += 1
                        elif valesona[valesona_tahejarg] != sona[sona_tahejarg]:
                            sona_tahejarg += 1
                protsendid.append(round(oigete_tahtede_arv/len(sona)*100))
                
            #kui valesona on võrdne
            elif len(valesona) == len(sona):
                for taht in sona:
                    if sona_tahejarg < len(sona):
                        if valesona[valesona_tahejarg] == sona[sona_tahejarg]:
                            oigete_tahtede_arv += 1
                            valesona_tahejarg += 1
                            sona_tahejarg += 1              
                protsendid.append(round(oigete_tahtede_arv/len(sona)*100))


    pot_oige = []
    sonade_arv = 0   
    for sona_1 in sobilikud_sonad:
        if sonade_arv < 3:
            it(protsendid, pot_oige, sobilikud_sonad)
            sonade_arv += 1
            
    return pot_oige


#test
#while True:
#    __input__ = str(input("Vale sõna: "))
#    print(autocorrect(__input__))
