fail = open("raamatukogu/lemmad2013.txt", encoding = "UTF-8")
for rida in fail:
    sisu = fail.read()
    sonastik = sisu.splitlines()

fail.close()

#listid
sonastik_lahti = []

#eraldab sõnastikus oleval sõnad tähtedeks
for sona in sonastik:
    sonastik_lahti_sona = list(sona)
    sonastik_lahti.append(sonastik_lahti_sona) 


def sona_protsent(x):
    #1
    potentsiaalne_oige = []
    parandatud_sonad = []
    sonastiku_sona_arv = -1 #
    vale_sona = list(x) #teeb vale-sona listiks ja võtab selle len-ni
    for OS in sonastik_lahti: #vaatab kas vale-sona 3 esimest tahte klappib oige-sona esimese 3 tahega sonastikus
        sonastiku_sona_arv +=1
        if len(OS) >= 3:
            if OS[0] == vale_sona[0] and OS[1] == vale_sona[1] and OS[2] == vale_sona[2] and len(OS) == len(vale_sona): #kui klappib votab oige sona len-ni ja kui see klappib lisab potentsaalsete sonade listi
                potentsiaalne_oige.append(sonastik[sonastiku_sona_arv])
    #print(potentsiaalne_oige) # testimiseks
    protsendid = []
    #2
    for pot_sona in potentsiaalne_oige: #hakkab taht taht haava vaatama sonu labi ja kui taht on sonas olemas lisab uhe punkti juurde
        pot_sona_lahti = list(pot_sona)
        tahe_arv = 3 #hakkab 4-ndast lugema
        oigete_tahtede_arv = 3 #olemas on juba 3 esimest tähte, mis on õiged
        for taht in pot_sona:
            if tahe_arv < len(vale_sona):
                if pot_sona_lahti[tahe_arv]== vale_sona[tahe_arv]:
                    oigete_tahtede_arv += 1
            tahe_arv += 1
        protsendid.append(round(oigete_tahtede_arv/len(vale_sona)*100)) #round(len(sona)/oigete_tahtede_arv) abil saab protsendi ja lisab protsentide listi
    #3
    #print(protsendid) # testimikseks
    #vaatab koige suurema protsendi väärtused ja lisab need listi
    for i in range(len(protsendid)):
        if protsendid[i] == max(protsendid):
            parandatud_sonad.append(potentsiaalne_oige[i])
    return parandatud_sonad

    
 
 
#test
#__input__ = str(input("Vale sõna: "))
#print(sona_protsent(__input__))

