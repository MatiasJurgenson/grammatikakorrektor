
#avab faili
fail = open("koostisosad/raamatukogu/lemmad2013.txt", encoding = "UTF-8")
for rida in fail:
    sisu = fail.read()
    sonastik = sisu.splitlines()

fail.close()

def oigekiri(sona):
    if sona in sonastik:
        return "true"
    
