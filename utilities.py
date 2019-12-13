def checkphone(telefono):

    lent = len(telefono)
    if lent == 9:
        return True
    else:
        return False

def checkID(DNI):

    lenDNI = len(DNI)
    if lenDNI == 9:
        auxDNI2 = DNI
    elif lenDNI == 8:
        auxDNI2 = "0" + DNI
    else:
        return False

    numDNI = auxDNI2[0:8]
    letteDNI = auxDNI2[8:9]

    if numDNI.isdigit() == False:
        return False

    if letteDNI.isalpha() == False:
        return False

    auxDNI = int(numDNI)

    letterDNI = letteDNI.upper()

    r = auxDNI % 23
    resto = int(r)

    if resto == 0 and letterDNI == "T":
        return True
    elif resto == 1 and letterDNI == "R":
        return True
    elif resto == 2 and letterDNI == "W":
        return True
    elif resto == 3 and letterDNI == "A":
        return True
    elif resto == 4 and letterDNI == "G":
        return True
    elif resto == 5 and letterDNI == "M":
        return True
    elif resto == 6 and letterDNI == "Y":
        return True
    elif resto == 7 and letterDNI == "F":
        return True
    elif resto == 8 and letterDNI == "P":
        return True
    elif resto == 9 and letterDNI == "D":
        return True
    elif resto == 10 and letterDNI == "X":
        return True
    elif resto == 11 and letterDNI == "B":
        return True
    elif resto == 12 and letterDNI == "N":
        return True
    elif resto == 13 and letterDNI == "J":
        return True
    elif resto == 14 and letterDNI == "Z":
        return True
    elif resto == 15 and letterDNI == "S":
        return True
    elif resto == 16 and letterDNI == "Q":
        return True
    elif resto == 17 and letterDNI == "V":
        return True
    elif resto == 18 and letterDNI == "H":
        return True
    elif resto == 19 and letterDNI == "L":
        return True
    elif resto == 20 and letterDNI == "C":
        return True
    elif resto == 21 and letterDNI == "K":
        return True
    elif resto == 22 and letterDNI == "E":
        return True
    else:
        return False
