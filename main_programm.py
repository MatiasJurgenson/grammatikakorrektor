#PROGRAMM TÖÖTAB WOOOOOOOOOOOOOOOOOOOOOO

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from koostisosad import main_sonastik
from koostisosad import lause_leidja
from koostisosad import koma_main
from koostisosad import autocorrect_main

#from main_programm import db
#db.create_all()
#from main_programm import Rawlaused
#Rawlaused.query.all()
#db.session.delete(Rawlaused.query.get())
#db.session.commit()
#Rawlaused.query.count()
#db.session.add()

#test lause = Ei sest, jah miks tud nud, aa o k. 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rawlaused.db'
app.config['SQLALCHEMY_BINDS'] = {'veakogu': 'sqlite:///rawvead.db'}
db = SQLAlchemy(app)

#database
class Rawlaused(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dblaused = db.Column(db.Text)
    def __repr__(self):
        return 'laused ' + str(self.id)
    
class Rawvead(db.Model):
    __bind_key__ = 'veakogu'
    id = db.Column(db.Integer, primary_key=True)
    dboige = db.Column(db.Text, nullable=False)
    dbviga_1 = db.Column(db.Text)
    dbviga_2 = db.Column(db.Text)
    dbviga_3 = db.Column(db.Text)
    lausearv = db.Column(db.Integer, nullable=False)
    sonaarv = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return 'viga ' + str(self.id)


#approute pealeht
@app.route('/', methods=['GET', 'POST'])
def index():
    
    vead = Rawvead.query.all()
    laused = Rawlaused.query.get_or_404(1)
    
    if request.method == 'POST':
        db.session.query(Rawlaused).delete()
        db.session.commit()
        p_pealkiri = request.form['pealkiri']
        uued_laused = Rawlaused(dblaused=p_pealkiri)
        db.session.add(uued_laused)
        db.session.commit()
        return redirect('/viga')
    else:
        return render_template('index.html', laused=laused, vead=vead)

#tekstianalüüs
@app.route('/viga', methods=['GET', 'POST'])
def lauseanaluus():        
     
    #definitions
    db.session.query(Rawvead).delete()
    db.session.commit()
    
    flaused = Rawlaused.query.get_or_404(1)
    lausenumber = 0
    veakohad = []
    õigesti = []
    sonakohad = []
    vea_arv = 0
    
    # lisada andmebaasist võtmine
    laused = lause_leidja.lause_avaja(flaused.dblaused)
    for lause in laused:
        sonanumber = 0
        for word in lause:
            wort = word.lower()
            sona = wort.replace(",", "") 
            if main_sonastik.oigekiri(sona) == None: # vaatab kas sõna on vale või õige
                
                veakohad.append(sona)
                õigesti.append(autocorrect_main.autocorrect(sona))
                
                if len(õigesti[vea_arv]) == 3:
                    sonasoovitused = õigesti[vea_arv]
                    sonasoov1 = sonasoovitused[0]
                    sonasoov2 = sonasoovitused[1]
                    sonasoov3 = sonasoovitused[2]
                    
                    sonakohad.append(sonanumber)
                    
                    oigedb = veakohad[vea_arv]
                
                    vigaprint = Rawvead(dboige=oigedb, dbviga_1=sonasoov1, dbviga_2=sonasoov2, dbviga_3=sonasoov3, lausearv=lausenumber, sonaarv=sonanumber)
                    db.session.add(vigaprint)
                    db.session.commit()
                    
                    vea_arv += 1
                    
                elif len(õigesti[vea_arv]) == 2:
                    sonasoovitused = õigesti[vea_arv]
                    sonasoov1 = sonasoovitused[0]
                    sonasoov2 = sonasoovitused[1]
                    
                    sonakohad.append(sonanumber)  
                    
                    oigedb = veakohad[vea_arv]
                
                    vigaprint = Rawvead(dboige=oigedb, dbviga_1=sonasoov1, dbviga_2=sonasoov2, lausearv=lausenumber, sonaarv=sonanumber)
                    db.session.add(vigaprint)
                    db.session.commit()
                    
                    vea_arv += 1
                    
                else:
                    sonasoovitused = õigesti[vea_arv]
                    sonasoov1 = sonasoovitused[0]
                    
                    sonakohad.append(sonanumber)
                    
                    oigedb = veakohad[vea_arv]
                
                    vigaprint = Rawvead(dboige=oigedb, dbviga_1=sonasoov1, lausearv=lausenumber, sonaarv=sonanumber)
                    db.session.add(vigaprint)
                    db.session.commit()
                    
                    vea_arv += 1
                      
            sonanumber += 1
        # komavea osa
        output = koma_main.komaviga(lause)
        asikoma = 1
        sama_vea_arv = 0
        
        for asi in output:
            if asikoma == 1:
                veakohad.extend(asi)
                asikoma = 2
            elif asikoma == 2:
                õigesti.extend(asi)
                asikoma = 3
            else:
                sonakohad.extend(asi)
       

        for viga in veakohad:
            if veakohad[sama_vea_arv] == õigesti[sama_vea_arv]:
                õigesti.pop(sama_vea_arv)
                veakohad.pop(sama_vea_arv)
                sonakohad.pop(sama_vea_arv)
                sama_vea_arv += 1
            else:
                sama_vea_arv += 1
        
        #mingil põhjusel lastes seda osa teist korda parandab see ühe buggi
        sama_vea_arv = 0
        for viga in veakohad:
            if veakohad[sama_vea_arv] == õigesti[sama_vea_arv]:
                õigesti.pop(sama_vea_arv)
                veakohad.pop(sama_vea_arv)
                sonakohad.pop(sama_vea_arv)
                sama_vea_arv += 1
            else:
                sama_vea_arv += 1
                
      # databasessi lisamine             
        for viga in veakohad:
            if vea_arv < len(veakohad):
                #teha komavigade lisamine databassie
                sonasoov1 = õigesti[vea_arv]
                
                sonakoht = sonakohad[vea_arv]
                       
                oigedb = veakohad[vea_arv]
                    
                vigaprint = Rawvead(dboige=oigedb, dbviga_1=sonasoov1, lausearv=lausenumber, sonaarv=sonakoht)
                db.session.add(vigaprint)
                db.session.commit()
                    
                vea_arv += 1
 
        lausenumber += 1
    return redirect('/')

#valesõna asendamine
@app.route('/asenda/<int:id>/1', methods=['GET', 'POST'])
def asenda_1(id):
    #võetakse db laused asendamiseks
    flaused = Rawlaused.query.get_or_404(1)
    laused = lause_leidja.lause_avaja(flaused.dblaused)
    #asendatav
    viganekoht = Rawvead.query.get_or_404(id)
    viga = viganekoht.dboige
    oige_ver = viganekoht.dbviga_1 # variant üks, sest valiti esimene variant
    lause_asukoht = viganekoht.lausearv
    sona_asukoht = viganekoht.sonaarv
    
    #vajalik esimesele (komavea parandus)
    komakoht = 2
    sonadearv = oige_ver.split()
    if len(sonadearv) == 2:
        if sonadearv[0][-1] == ",":
            komakoht = 1
        else:
            komakoht = 0
            
    asendatav_sona = laused[lause_asukoht][sona_asukoht]
    if komakoht == 1:
        if len(asendatav_sona) >= 3 and asendatav_sona[-3] == "t" and asendatav_sona[-2] == "u" and asendatav_sona[-1] == "d" or len(asendatav_sona) >= 3 and asendatav_sona[-3] == "n" and asendatav_sona[-2] == "u" and asendatav_sona[-1] == "d":
            parandus = (asendatav_sona + ",")
            laused[lause_asukoht][sona_asukoht] = parandus
            
        else:
            x = sona_asukoht - 1
            asendatav_sona = laused[lause_asukoht][x]
            parandus = (asendatav_sona + ",")
            laused[lause_asukoht][x] = parandus
            
    elif komakoht == 0:
        x = sona_asukoht - 1
        asendatav_sona = laused[lause_asukoht][x]
        parandus = asendatav_sona.replace(",", "")
        laused[lause_asukoht][x] = parandus
        
    #s]navea parandus    
    elif komakoht == 2:
        if laused[lause_asukoht][sona_asukoht][-1] == ",":
            laused[lause_asukoht][sona_asukoht] = (oige_ver + ",")
        else:
            laused[lause_asukoht][sona_asukoht] = oige_ver
               
    valmis_laused = []
    for lause in laused:
        lause1 = ' '.join(map(str, lause[:-1]))
        lause2 = (lause1 + (str(lause[-1])))
        valmis_laused.append(lause2)

    valmis = ' '.join(map(str, valmis_laused))
    
    #vea ja lause kustutamine
    db.session.delete(viganekoht)
    db.session.query(Rawlaused).delete()
    db.session.commit()
    
    #uue lause lisamine
    uued_laused = Rawlaused(dblaused=valmis)
    db.session.add(uued_laused)
    db.session.commit()
     
    return redirect('/')

@app.route('/asenda/<int:id>/2', methods=['GET', 'POST'])
def asenda_2(id):  
    #võetakse db laused asendamiseks
    flaused = Rawlaused.query.get_or_404(1)
    laused = lause_leidja.lause_avaja(flaused.dblaused)
    #asendatav
    viganekoht = Rawvead.query.get_or_404(id)
    viga = viganekoht.dboige
    oige_ver = viganekoht.dbviga_2 # variant kaks, sest valiti teine variant
    lause_asukoht = viganekoht.lausearv
    sona_asukoht = viganekoht.sonaarv
    
    if laused[lause_asukoht][sona_asukoht][-1] == ",":
        laused[lause_asukoht][sona_asukoht] = (oige_ver + ",")
    else:
        laused[lause_asukoht][sona_asukoht] = oige_ver
        
    valmis_laused = []
    for lause in laused:
        lause1 = ' '.join(map(str, lause[:-1]))
        lause2 = (lause1 + (str(lause[-1])))
        valmis_laused.append(lause2)

    valmis = ' '.join(map(str, valmis_laused))
    
    #vea ja lause kustutamine
    db.session.delete(viganekoht)
    db.session.query(Rawlaused).delete()
    db.session.commit()
    
    #uue lause lisamine
    uued_laused = Rawlaused(dblaused=valmis)
    db.session.add(uued_laused)
    db.session.commit()

    return redirect('/')

@app.route('/asenda/<int:id>/3', methods=['GET', 'POST'])
def asenda_3(id):    
    #võetakse db laused asendamiseks
    flaused = Rawlaused.query.get_or_404(1)
    laused = lause_leidja.lause_avaja(flaused.dblaused)
    #asendatav
    viganekoht = Rawvead.query.get_or_404(id)
    viga = viganekoht.dboige
    oige_ver = viganekoht.dbviga_3 # variant kom, sest valiti kolmas variant
    lause_asukoht = viganekoht.lausearv
    sona_asukoht = viganekoht.sonaarv
    
    if laused[lause_asukoht][sona_asukoht][-1] == ",":
        laused[lause_asukoht][sona_asukoht] = (oige_ver + ",")
    else:
        laused[lause_asukoht][sona_asukoht] = oige_ver
        
    valmis_laused = []
    for lause in laused:
        lause1 = ' '.join(map(str, lause[:-1]))
        lause2 = (lause1 + (str(lause[-1])))
        valmis_laused.append(lause2)

    valmis = ' '.join(map(str, valmis_laused))
    
    #vea ja lause kustutamine
    db.session.delete(viganekoht)
    db.session.query(Rawlaused).delete()
    db.session.commit()
    
    #uue lause lisamine
    uued_laused = Rawlaused(dblaused=valmis)
    db.session.add(uued_laused)
    db.session.commit()
    
    return redirect('/')

#vea kustutamine
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def kustuta(id):
    viganekoht = Rawvead.query.get_or_404(id)
    db.session.delete(viganekoht)
    db.session.commit()
    return redirect('/')

#debugger 
if __name__ == "__main__":
    app.run(debug=True)