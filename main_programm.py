from koostisosad import main_sonastik
from koostisosad import lause_leidja

#definitions
laused = []

#"""_____"""#

while True:
    tekst = str(input(""))
    laused = lause_leidja.lause_avaja(tekst)
#    print(laused)
    for lause in laused:
        for sona in lause:
            print(main_sonastik.oigekiri(sona))

#lause leidja
#sonastik

#autocorrect
#teised pudipadi reeglid
