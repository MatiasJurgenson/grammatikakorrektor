import re
#LLM = lause lõpu märk

#võtab LLM-i sõna lõpust ära
def LLS(x):
    list2 = list(x)
    if list2[-1] == "." or list2[-1] == "!" or list2[-1] == "?":
        y = x[:-1]
        return y
    else:
        return x

#teeeb teksti lauseteks
def lause_avaja(tekst):
    erandid = ['e.m.a','k.a','m.a.j','p.o','s.a','s.o','s.t','v.a']
    lause = []
    laused = []
    lause_sonad = []
    LLM = []
    tekstid = []
    tekstid = tekst.split()
    for sona in tekstid:
        sona_LLM_puudub = LLS(sona)
        SONA = list(sona)
        if SONA[-1] == "." or SONA[-1] == "!" or SONA[-1] == "?":           
            lause.append(sona_LLM_puudub)
            lause.append(SONA[-1])
            laused.append(lause)
            lause = []
        else:
            lause.append(sona)
    return laused


#for testing

#while True:
#    tekst = str(input(""))
#    laused = lause_avaja(tekst)
#    print(laused)
#    print(tekst)
