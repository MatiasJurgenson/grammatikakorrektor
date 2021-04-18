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
    komaveakohad = []
    komaõigesti = []
    sonakoht = []
    sonanumber = 0

    for word in lause:
        komata_sona = word.replace(",", "")
        # koma ette panemine
        if komata_sona in komaga or komata_sona == "kui" and lause[lause.index(komata_sona)+1] != "ka":
            x = lause.index(word)
            x -= 1
            if lause[x][-1] != ",":
                komaveakohad.append(lause[x] + " " + lause[x + 1])
                komaette = (lause[x] + ",")
                komaõigesti.append(komaette + " " + lause[x + 1 ])
                sonakoht.append(sonanumber)
        # nud/tud        
        elif len(komata_sona) >= 3 and komata_sona[-3] == "t" and komata_sona[-2] == "u" and komata_sona[-1] == "d" or len(komata_sona) >= 3 and komata_sona[-3] == "n" and komata_sona[-2] == "u" and komata_sona[-1] == "d":
            if komata_sona != lause[0] or komata_sona != lause[-1]:
                x = lause.index(word)
                komaette = (komata_sona + ",")
                komaveakohad.append(lause[x] + " " + lause[x + 1])
                komaõigesti.append(komaette + " " + lause[x + 1])
                sonakoht.append(sonanumber)
        # koma ära võtmine            
        elif word in komata_sidesonad or word == "kui" and lause[lause.index(word)+1] == "ka" or komata_sona not in komaga:
            x = lause.index(word)
            x -= 1
            if lause[x][-1] == "," and len(lause[x]) >= 4 and lause[x][-4] != "t" and lause[x][-3] != "u" and lause[x][-2] != "d" or len(lause[x]) >= 4 and lause[x][-4] != "n" and lause[x][-3] != "u" and lause[x][-2] != "d":
                
                asendatav_sona = lause[x]
                asendatav_sona = asendatav_sona.replace(",", "")
                komaveakohad.append(lause[x] + " " + lause[x + 1])
                komaõigesti.append(asendatav_sona + " " + lause[x + 1 ])
                sonakoht.append(sonanumber)
                
        sonanumber += 1       
                        
    return [komaveakohad, komaõigesti, sonakoht]