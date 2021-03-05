# probleem komaviga automaatselt parandab lause ära kuigi ei tohiks seda teha


from koostisosad import lause_leidja


fail = open("koostisosad/raamatukogu/komaga.txt", encoding = "UTF-8")
for rida in fail:
    sisu = fail.read()
    komaga = sisu.splitlines()

fail.close()

#lause_1 = "Ei sest, jah miks tud nud, aa o k."
#lause_2 = "Ei, sest jah, miks tud, nud, aa o k."

#komaga
#Kiri valmis kirjutatud, jäi tüdruk mõtlema. tud/nud
# eemaldada koma: ehk, nii... kui ka, ja, ning, või

komata_sidesonad = ["ehk", "nii", "ja", "ning", "või"]

def komaviga(lause):
    p_lause = lause
    for word in p_lause:
        komata_sona = word.replace(",", "")
        if komata_sona in komaga or komata_sona == "kui" and p_lause[p_lause.index(komata_sona)+1] != "ka":
            x = p_lause.index(word)
            x -= 1
            komaette = (p_lause[x] + ",")
            p_lause[x] = komaette
                
        elif len(komata_sona) >= 3 and komata_sona[-3] == "t" and komata_sona[-2] == "u" and komata_sona[-1] == "d" or len(komata_sona) >= 3 and komata_sona[-3] == "n" and komata_sona[-2] == "u" and komata_sona[-1] == "d":
            if komata_sona != p_lause[0] or komata_sona != p_lause[-1]:
                x = p_lause.index(word)
                komaette = (komata_sona + ",")
                p_lause[x] = komaette
                    
        elif word in komata_sidesonad or word == "kui" and p_lause[p_lause.index(word)+1] == "ka" or word.replace(",", "") not in komaga:
            x = p_lause.index(word)
            x -= 1
            if p_lause[x][-1] == "," and len(p_lause[x]) >= 3 and p_lause[x][-4] != "t" and p_lause[x][-3] != "u" and p_lause[x][-2] != "d" or len(p_lause[x]) >= 3 and p_lause[x][-4] != "n" and p_lause[x][-3] != "u" and p_lause[x][-2] != "d":
                asendatav_sona = p_lause[x]
                asendatav_sona = asendatav_sona.replace(",", "")
                p_lause[x] = asendatav_sona
                
                        
    return p_lause
            
#i = 1                       
#laused = lause.lause_avaja(lause_1)
#print(' '.join(map(str, laused)))
#for lause in laused:
#    komaviga(lause)
#    print(' '.join(map(str, lause[0:-1])) + lause[-1])
#    print(lause_2)