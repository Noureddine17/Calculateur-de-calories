from bottle import route, run, request, template, static_file

@route("/page")

def html():

    return template(r"C:\Users\maroc\Desktop\ECOLE\Nouveau.dossier\fichier.html")

@route('/static/<filename:path>')

def css(filename):

    return static_file(filename, root= r'C:\Users\maroc\Desktop\ECOLE\Nouveau.dossier\static')


@route("/resultat", method="post")

def index2():

    age = request.forms.get("age")

    poids = request.forms.get("poids")

    tailles = request.forms.get("tailles")

    sexe = request.forms.get("sexe")

    niveau = request.forms.get("niveau")

    objectif = request.forms.get("objectif")

    if sexe == "Homme":

        return  MH(tailles,poids,age,niveau,objectif)

    if sexe == "Femme":

        return  MF(tailles,poids,age,niveau,objectif)


def MH(tailles, poids, age, niveau, objectif):

    resultat=""

    A = float(poids) * 13.7

    B = float(tailles) * 5

    C = float(age) * 6.8

    D = A + B + 66.46

    E = D - C

    if niveau == "Sedentaire":

        Z =  E * 1.2

    elif niveau == "Legerement actif":

        Z = E * 1.375

    elif niveau == "Actif":

        Z = E * 1.55

    elif niveau == "Tres Actif":

        Z = E * 1.725

    elif niveau == "Extremement actif":

        Z =  E * 1.9

    V = round(Z)

    if objectif == "Perte de Poids":

        resultat = str(round(V*0.9))

        return template(r"C:\Users\maroc\Desktop\ECOLE\Nouveau.dossier\fichier2.html",resultat=resultat)

    elif objectif == "Garder la Ligne":

        resultat =  str(V)

        return template(r"C:\Users\maroc\Desktop\ECOLE\Nouveau.dossier\fichier4.html",resultat=resultat)


    elif objectif == "Prise de Masse":

        resultat = str(round(V*1.1))

        return template(r"C:\Users\maroc\Desktop\ECOLE\Nouveau.dossier\fichier3.html", resultat =resultat)


def MF(tailles, poids, age,niveau,objectif):

    resultat=""

    A = float(poids) * 9.6

    B = float(tailles) * 1.8

    C = float(age) * 4.7

    D = A + B + 655.1

    E = D - C

    if niveau == "Sedentaire":

        Z =  E * 1.2

    elif niveau =="Legerement actif":

        Z = E*1.375

    elif niveau == "Actif":

        Z = E * 1.55


    elif niveau == "Tres Actif":

        Z = E * 1.725


    elif niveau == "Extremement actif":

        Z =  E * 1.9

    V = round(Z)

    if objectif == "Perte de Poids":

        resultat = str(round(V*0.9))

        return template(r"C:\Users\maroc\Desktop\ECOLE\Nouveau.dossier\fichier2.html",resultat=resultat)

    elif objectif == "Garder la Ligne":

        resultat =  str(V)

        return template(r"C:\Users\maroc\Desktop\ECOLE\Nouveau.dossier\fichier4.html",resultat=resultat)

    elif objectif == "Prise de Masse":

        resultat = str(round(V*1.1))

        return template(r"C:\Users\maroc\Desktop\ECOLE\Nouveau.dossier\fichier3.html", resultat =resultat)

run(host="localhost", port=8080)