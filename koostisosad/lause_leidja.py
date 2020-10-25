import re

#tuleb lisada erandid(lühendid)
#tuleb removeda LLM - ga list


#algversioon

#def lause_avaja(tekst):
#    #vaatab lauselõpumärke
#    for sona in tekst:
#        #if sona != listis erandid
#        for taht in sona:
#            if taht == ".":  
#                LLM.append(taht)
#            elif taht == "!":
#                LLM.append(taht)
#            elif taht == "?":
#                LLM.append(taht)
#
#    #eraldab teksti lauseteks ja lisab lauselõpumärgi
#    eraldus = re.split('[.!?]',tekst)
#    if "" in eraldus:    
#        eraldus.remove("")
#    i = 0
#    for lause in eraldus:
#        lausetu = lause.split()
#        if len(LLM) != 0 and len(LLM) > i:    
#            lausetu.append(LLM[i])
#        laused.append(lausetu)
#        i +=1
#    return laused


#new and improved (hopefully)

def lause_avaja(tekst):
    lause = []
    laused = []
    lause_sonad = []
    LLM = []
    tekstid = []
    tekstid = tekst.split()
    for sona in tekstid:
        for taht in sona:
            if taht == "." or taht == "!" or taht == "?": #and sona not in erandid
                eraldus = re.split('[.!?]',sona)
                if "" in eraldus:    
                    eraldus.remove("")
                lause.append(eraldus)
                lause.append(taht)
                laused.append(lause)
                lause = []
        if taht != "." and taht != "!" and taht != "?":
            lause.append(sona)
    return laused


#for testing

#while True:
#    tekst = str(input(""))
#    laused = lause_avaja(tekst)
#    print(laused)
