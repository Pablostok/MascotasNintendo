import print_menus
import utilities
import codecs

#########################################################################################
clientName = []
clientSurname = []
clientID = []
clientPhone = []
clientPet = []
#########################################################################################-
petOwner = []
petName = []
petKind = []
petGenre = []
#########################################################################################
def refresh():
    ruta = '.\\data\\'
    i = 1

    with open(ruta + "clientes.txt", 'r') as reader:
        for line in reader:
            if i == 1:
                clientName.append(line[:-1])
            elif i == 2:
                clientSurname.append(line[:-1])
            elif i == 3:
                clientID.append(line[:-1])
            elif i == 4:
                clientPhone.append(line[:-1])
            elif i == 5:
                cp = int(line[:-1])
                clientPet.append(cp)
            i = i + 1
            if i == 6:
                i = 1

    i = 1

    with open(ruta + "mascotas.txt", 'r') as reader:
        for line in reader:
            if i == 1:
                petName.append(line[:-1])
            elif i == 2:
                petOwner.append(line[:-1])
            elif i == 3:
                petKind.append(line[:-1])
            elif i == 4:
                petGenre.append(line[:-1])
            i = i + 1
            if i == 5:
                i = 1


def saveclien():
    ruta = '.\\data\\'
    file = open(ruta + "clientes.txt", "w")

    leido = len(clientName)

    for i in range(0, leido):
        file.write(clientName[i] + "\n")
        file.write(clientSurname[i] + "\n")
        file.write(clientID[i] + "\n")
        file.write(clientPhone[i] + "\n")
        cp = str(clientPet[i])
        file.write(cp + "\n")

    file.close()


def savemasc():
    ruta = '.\\data\\'
    file = open(ruta + "mascotas.txt", "w")

    leido = len(petOwner)

    for i in range(0, leido):
        file.write(petName[i] + "\n")
        file.write(petOwner[i] + "\n")
        file.write(petKind[i] + "\n")
        file.write(petGenre[i] + "\n")

    file.close()


def main():
    print_menus.principalmenu()
    ok = False
    while ok == False:

        num = input("Introduzca número: ")

        if num == "1":
            # funcion horario hoy
            ok = True
        elif num == "2":
            # funcion calendario
            ok = True
        elif num == "3":
            # funcion citas
            ok = True
        elif num == "4":
            clientes()
            ok = True
        elif num == "5":
            mascotas()
            ok = True
        elif num == "9":
            saveclien()
            savemasc()
            exit(9)


def editclien():
    print_menus.editclien1()
    mostrarclientes()
    print("")
    nu = input("Introduzca el número del cliente a editar: ")
    num = int(nu)
    print("")
    i = num
    o = str(i)
    print(o + ". " + clientName[i] + " " + clientSurname[i])
    print("   " + "DNI:      " + clientID[i])
    print("   " + "Teléfono: " + clientPhone[i])
    devmasc(i)
    print("")

    ok = False
    while ok == False:
        print("   ---¿Quiere editar a este cliente?---   ")
        resp = input("S/N: ")

        if resp.upper() == "S":
            editaclien(i)
            ok = True
        elif resp.upper() == "N":
            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de edición (E) o al de clientes (C)?---")
                print("")
                resp = input("Introduzca E o M: ")
                if resp.upper() == "E":
                    editclien()
                    ook = True
                elif resp.upper() == "M":
                    clientes()
                    ook = True
            ok = True


def editaclien(num):
    print_menus.editclien2()
    ok = False
    while ok == False:
        print()
        nu = input("Introduzca número: ")

        aux = int(nu)

        if nu == "1":
            edinombrec(num)
            ok = True
        elif nu == "2":
            edittelc(num)
            ok = True


def edinombrec(num):
    print("")
    print("")
    nom = input("Introduzca el nuevo nombre del cliente: ")
    ap = input("Introduzca el nuevo apellido del cliente: ")
    print("")
    print("Estás seguro de que quieres cambiar el nombre de: "+ averiguarNom(clientID[num]) + " a este: " + nom + " " + ap)
    ok = False
    while ok == False:
        res = input("S/N: ")
        if res.upper() == "S":
            ID = clientID[num]
            Tel = clientPhone[num]
            pet = clientPet[num]
            del (clientName[num])
            del (clientSurname[num])
            del (clientID[num])
            del (clientPhone[num])
            del (clientPet[num])

            clientName.append(nom)
            clientSurname.append(ap)
            clientID.append(ID)
            clientPhone.append(Tel)
            clientPet.append(pet)
            print("")
            print("   ---Modificado corréctamente---   ")
            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de edición (E) o al de clientes (C)?---")
                print("")
                resp = input("Introduzca E o C: ")
                if resp.upper() == "E":
                    editclien()
                    ook = True
                elif resp.upper() == "C":
                    clientes()
                    ook = True
            ok = True
        elif res.upper() == "N":
            print("")
            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de edición (E) o al de clientes (C)?---")
                print("")
                resp = input("Introduzca E o C: ")
                if resp.upper() == "E":
                    editclien()
                    ook = True
                elif resp.upper() == "C":
                    clientes()
                    ook = True
            ok = True


def edittelc(num):
    print("")
    print("")
    ok = False
    while ok == False:
        tel = input("Introduzca el nuevo teléfono del cliente: ")
        ook = utilities.checkphone(tel)
        if ook == True:
            ok = True

    print("")
    print("Estás seguro de que quieres cambiar el teléfono del cliente: "+ averiguarNom(clientID[num]) +" - " + clientID[num] + " de este: " + clientPhone[num] +" a este: " + tel)
    ok = False
    while ok == False:
        res = input("S/N: ")
        if res.upper() == "S":
            nom = clientName[num]
            sur = clientSurname[num]
            ID = clientID[num]
            pet = clientPet[num]
            del (clientName[num])
            del (clientSurname[num])
            del (clientID[num])
            del (clientPhone[num])
            del (clientPet[num])

            clientName.append(nom)
            clientSurname.append(sur)
            clientID.append(ID)
            clientPhone.append(tel)
            clientPet.append(pet)
            print("")
            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de edición (E) o al de clientes (C)?---")
                print("")
                resp = input("Introduzca E o C: ")
                if resp.upper() == "E":
                    editclien()
                    ook = True
                elif resp.upper() == "C":
                    clientes()
                    ook = True
            ok = True
            print("   ---Modificado corréctamente---   ")
        elif res.upper() == "N":
            print("")
            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de edición (E) o al de clientes (C)?---")
                print("")
                resp = input("Introduzca E o C: ")
                if resp.upper() == "E":
                    editclien()
                    ook = True
                elif resp.upper() == "C":
                    clientes()
                    ook = True
            ok = True


def editmasc():
    print_menus.editmasc1()
    mostrarmasc()
    print("")
    nu = input("Introduzca el número de la mascota a editar: ")
    num = int(nu)
    print("")
    i = num
    o = str(i)
    print(o + ". " + petName[i] + "(" + petGenre[i] + ")")
    print("   " + "Raza:  " + petKind[i])
    nombre = averiguarNom(petOwner[i])
    print("   " + "Dueño: " + petOwner[i] + " - " + nombre)
    print("")
    print("")

    ok = False
    while ok == False:
        print("   ---¿Quiere editar a esta mascota?---   ")
        resp = input("S/N: ")

        if resp.upper() == "S":
            editamasc(i)
            ok = True
        elif resp.upper() == "N":
            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de edición (E) o al de mascotas (M)?---")
                print("")
                resp = input("Introduzca E o M: ")
                if resp.upper() == "E":
                    editmasc()
                    ook = True
                elif resp.upper() == "M":
                    mascotas()
                    ook = True
            ok = True


def editamasc(num):
    print_menus.editmasc2()
    ok = False
    while ok == False:
        print()
        nu = input("Introduzca número: ")
        aux = int(nu)

        if nu == "1":
            editnombrem(num)
            ok = True
        elif nu == "2":
            editraza(num)
            ok = True
        elif nu == "3":
            editsexo(num)
            ok = True
        elif nu == "4":
            editduenio(num)
            ok = True


def editduenio(num):
    print("")
    print("")
    ok = False
    while ok == False:
        dni = input("Introduzca el DNI del nuevo dueño de la mascota: ")
        ook = utilities.checkID(dni)
        if ook == True:
            ok = True
    print("")
    print("Estás seguro de que quieres cambiar el dueño de la mascota: "+ petName[num] + "(" + petGenre[num] + ")" +" - " + petKind[num] + " del cliente: " + averiguarNom(petOwner[num]) + " - " + petOwner[num] + " al cliente: ")
    nuum = devnum(dni)
    verclien(nuum)
    aux = devnum(num)
    ok = False
    while ok == False:
        res = input("S/N: ")
        if res.upper() == "S":
            nom = petName[num]
            ID = clientID[nuum]
            gen = petGenre[num]
            kind = petKind[num]
            del (petName[num])
            del (petOwner[num])
            del (petGenre[num])
            del (petKind[num])
            clientPet[aux] = clientPet[aux] - 1
            clientPet[nuum] = clientPet[nuum] + 1

            petName.append(nom)
            petOwner.append(ID)
            petGenre.append(gen)
            petKind.append(kind)
            print("")
            print("   ---Modificado corréctamente---   ")
            print("")
            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de edición (E) o al de mascotas (M)?---")
                print("")
                resp = input("Introduzca E o M: ")
                if resp.upper() == "E":
                    editclien()
                    ook = True
                elif resp.upper() == "M":
                    mascotas()
                    ook = True
            ok = True
        elif res.upper() == "N":
            print("")
        elif res.upper() == "N":
            print("")
            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de edición (E) o al de mascotas (M)?---")
                print("")
                resp = input("Introduzca E o M: ")
                if resp.upper() == "E":
                    editclien()
                    ook = True
                elif resp.upper() == "M":
                    mascotas()
                    ook = True
            ok = True


def verclien(i):
    o = str(i)
    print(o + ". " + clientName[i] + " " + clientSurname[i])
    print("   " + "DNI:      " + clientID[i])
    print("   " + "Teléfono: " + clientPhone[i])
    devmasc(i)
    print("")


def editnombrem(num):
    print("")
    print("")
    nom = input("Introduzca el nuevo nombre de la mascota: ")
    print("")
    print("Estás seguro de que quieres cambiar el nombre de la mascota: "+ petName[num] + "(" + petGenre[num] + ")" +" - " + petKind[num] + " del cliente: " + averiguarNom(petOwner[num]) + " - " + petOwner[num] + " a este: " + nom)
    ok = False
    while ok == False:
        res = input("S/N: ")
        if res.upper() == "S":
            ID = petOwner[num]
            gen = petGenre[num]
            kind = petKind[num]
            del (petName[num])
            del (petOwner[num])
            del (petGenre[num])
            del (petKind[num])

            petName.append(nom)
            petOwner.append(ID)
            petGenre.append(gen)
            petKind.append(kind)
            print("")
            print("   ---Modificado corréctamente---   ")
            print("")
            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de edición (E) o al de mascotas (M)?---")
                print("")
                resp = input("Introduzca E o M: ")
                if resp.upper() == "E":
                    editclien()
                    ook = True
                elif resp.upper() == "M":
                    mascotas()
                    ook = True
            ok = True
        elif res.upper() == "N":
            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de edición (E) o al de mascotas (M)?---")
                print("")
                resp = input("Introduzca E o M: ")
                if resp.upper() == "E":
                    editclien()
                    ook = True
                elif resp.upper() == "M":
                    mascotas()
                    ook = True
            ok = True


def editraza(num):
    print("")
    print("")
    kind = input("Introduzca la nueva raza de la mascota: ")
    print("")
    print("Estás seguro de que quieres cambiar la raza de la mascota: "+ petName[num] + "(" + petGenre[num] + ")" +" - " + petKind[num] + " del cliente: " + averiguarNom(petOwner[num]) + " - " + petOwner[num] + " a esta: " + kind)
    ok = False
    while ok == False:
        res = input("S/N: ")
        if res.upper() == "S":
            nom = petName[num]
            ID = petOwner[num]
            gen = petGenre[num]
            del (petName[num])
            del (petOwner[num])
            del (petGenre[num])
            del (petKind[num])

            petName.append(nom)
            petOwner.append(ID)
            petGenre.append(gen)
            petKind.append(kind)
            print("")
            print("   ---Modificado corréctamente---   ")
            print("")
            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de edición (E) o al de mascotas (M)?---")
                print("")
                resp = input("Introduzca E o M: ")
                if resp.upper() == "E":
                    editclien()
                    ook = True
                elif resp.upper() == "M":
                    mascotas()
                    ook = True
            ok = True
        elif res.upper() == "N":
            print("")
        elif res.upper() == "N":
            print("")
            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de edición (E) o al de mascotas (M)?---")
                print("")
                resp = input("Introduzca E o M: ")
                if resp.upper() == "E":
                    editclien()
                    ook = True
                elif resp.upper() == "M":
                    mascotas()
                    ook = True
            ok = True


def editsexo(num):
    print("")
    print("")
    gen = input("Introduzca el nuevo sexo de la mascota: ")
    print("")
    print("Estás seguro de que quieres cambiar el género de la mascota: "+ petName[num] + "(" + petGenre[num] + ")" +" - " + petKind[num] + " del cliente: " + averiguarNom(petOwner[num]) + " - " + petOwner[num] + " a este: " + gen)
    ok = False
    while ok == False:
        res = input("S/N: ")
        if res.upper() == "S":
            nom = petName[num]
            ID = petOwner[num]
            kind = petKind[num]
            del (petName[num])
            del (petOwner[num])
            del (petGenre[num])
            del (petKind[num])

            petName.append(nom)
            petOwner.append(ID)
            petGenre.append(gen)
            petKind.append(kind)
            print("")
            print("   ---Modificado corréctamente---   ")
            print("")

            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de edición (E) o al de mascotas (M)?---")
                print("")
                resp = input("Introduzca E o M: ")
                if resp.upper() == "E":
                    editclien()
                    ook = True
                elif resp.upper() == "M":
                    mascotas()
                    ook = True
            ok = True
        elif res.upper() == "N":
            print("")
        elif res.upper() == "N":
            print("")
            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de edición (E) o al de mascotas (M)?---")
                print("")
                resp = input("Introduzca E o M: ")
                if resp.upper() == "E":
                    editclien()
                    ook = True
                elif resp.upper() == "M":
                    mascotas()
                    ook = True
            ok = True


def devmasc(numclien):
    nummasc = clientPet[numclien]

    leido = len(clientID)

    if nummasc != 0:

        cont = 0

        for i in range(0, numclien):
            cont = cont + clientPet[i]

        posfinal = cont + nummasc

        num = 1

        for i in range(cont, posfinal):
            o = str(num)
            print("   " + "Pet " + o + ": " + petName[i] + " - " + petKind[i] + "(" + petGenre[i] + ")")
            num = num + 1


def averiguarNom(DNI):
    leido = len(clientID)
    aux = ""

    for i in range(0, leido):
        if DNI == clientID[i]:
            aux = clientName[i] + " " + clientSurname[i]
    return aux


def devnum(DNI):
    leido = len(clientID)
    aux = 0

    for i in range(0, leido):
        if DNI == clientID[i]:
            aux = i
    return aux


def mascotas():
    print_menus.menumasc()
    ok = False
    while ok == False:
        num = input("Introduzca número: ")

        if num == "1":
            mostrarmasc()
            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de mascotas (M) o al principal (P)?---")
                print("")
                resp = input("Introduzca M o P: ")
                if resp.upper() == "M":
                    mascotas()
                    ook = True
                elif resp.upper() == "P":
                    main()
                    ook = True
            ok = True
        elif num == "2":
            altamasc()
            ok = True
        elif num == "3":
            bajamasc()
            ok = True
        elif num == "4":
            buscamasc()
            ok = True
        elif num == "5":
            editmasc()
            ok = True
        elif num == "9":
            main()
            ok = True


def mostrarmasc():
    print("")
    leido = len(petOwner)

    for i in range(0, leido):
        o = str(i)
        print(o + ". " + petName[i] + "(" + petGenre[i] + ")")
        print("   " + "Raza:  " + petKind[i])
        nombre = averiguarNom(petOwner[i])
        print("   " + "Dueño: " + petOwner[i] + " - " + nombre)
        print("")


def buscaduenio():
    print("")

    ok = False

    while ok == False:
        DNI = input("Introduzca DNI del dueño: ")
        okis = utilities.checkID(DNI)
        if okis == True and DNI in petOwner:
            ok = True

    print("")

    leido = len(petOwner)

    for i in range(0, leido):
        if DNI.upper() in petOwner[i]:
            print("")
            o = str(i)
            print(o + ". " + petName[i] + "(" + petGenre[i] + ")")
            print("   " + "Raza:  " + petKind[i])
            nombre = averiguarNom(petOwner[i])
            print("   " + "Dueño: " + petOwner[i] + " - " + nombre)
            print("")

    ook = False
    while ook == False:
        print("---¿Quieres volver a la busqueda (B) o al menú de mascotas (M)?---")
        print("")
        resp = input("Introduzca B o M: ")
        if resp.upper() == "B":
            buscamasc()
            ook = True
        elif resp.upper() == "M":
            mascotas()
            ook = True


def buscanombreM():
    print("")
    ok = False
    while ok == False:
        nom = input("Introduzca el nombre de la mascota: ")
        print("")

        leido = len(petName)

        cont = 0

        for i in range(0, leido):
            if nom.upper() in petName[i].upper():
                print("")
                o = str(i)
                print(o + ". " + petName[i] + "(" + petGenre[i] + ")")
                print("   " + "Raza:  " + petKind[i])
                nombre = averiguarNom(petOwner[i])
                print("   " + "Dueño: " + petOwner[i] + " - " + nombre)
                print("")
                cont = cont + 1

        if cont == 0:
            print("   ---No existen mascotas con ese nombre---   ")
            print("")
            ok = True
        else:
            ok = True

    ook = False
    while ook == False:
        print("---¿Quieres volver a la busqueda (B) o al menú de mascotas (M)?---")
        print("")
        resp = input("Introduzca B o M: ")
        if resp.upper() == "B":
            buscamasc()
            ook = True
        elif resp.upper() == "M":
            mascotas()
            ook = True


def buscaraza():
    print("")
    ok = False
    while ok == False:
        kind = input("Introduzca la raza de la mascota: ")
        print("")

        leido = len(petKind)

        cont = 0

        for i in range(0, leido):
            if kind.upper() in petKind[i].upper():
                print("")
                o = str(i)
                print(o + ". " + petName[i] + "(" + petGenre[i] + ")")
                print("   " + "Raza:  " + petKind[i])
                nombre = averiguarNom(petOwner[i])
                print("   " + "Dueño: " + petOwner[i] + " - " + nombre)
                print("")
                cont = cont + 1

        if cont == 0:
            print("   ---No existen mascotas con esa raza---   ")
            print("")
            ok = True
        else:
            ok = True

    ook = False
    while ook == False:
        print("---¿Quieres volver a la busqueda (B) o al menú de mascotas (M)?---")
        print("")
        resp = input("Introduzca B o M: ")
        if resp.upper() == "B":
            buscamasc()
            ook = True
        elif resp.upper() == "M":
            mascotas()
            ook = True


def buscagenero():
    print("")
    ok = False
    while ok == False:
        gen = input("Introduzca el sexo de la mascota: ")
        print("")

        leido = len(petGenre)

        cont = 0

        for i in range(0, leido):
            if gen.upper() in petGenre[i].upper():
                print("")
                o = str(i)
                print(o + ". " + petName[i] + "(" + petGenre[i] + ")")
                print("   " + "Raza:  " + petKind[i])
                nombre = averiguarNom(petOwner[i])
                print("   " + "Dueño: " + petOwner[i] + " - " + nombre)
                print("")
                cont = cont + 1

        if cont == 0:
            print("   ---No existen mascotas con ese sexo---   ")
            print("")
            ok = True
        else:
            ok = True

    ook = False
    while ook == False:
        print("---¿Quieres volver a la busqueda (B) o al menú de mascotas (M)?---")
        print("")
        resp = input("Introduzca B o M: ")
        if resp.upper() == "B":
            buscamasc()
            ook = True
        elif resp.upper() == "M":
            mascotas()
            ook = True


def buscamasc():
    print_menus.buscamasc()
    print("")

    ok = False

    while ok == False:
        resp = input("Introduzca número: ")
        print("")
        if resp == "1":
            buscaduenio()
            ok = True

        elif resp == "2":
            buscanombreM()
            ok = True

        elif resp == "3":
            buscaraza()
            ok = True

        elif resp == "4":
            buscagenero()
            ok = True

        elif resp == "9":
            mascotas()
            ok = True


def bajamasc():
    print_menus.bajamasc()
    print("")
    leido = len(petOwner)

    for i in range(0, leido):
        o = str(i)
        print(o + ". " + petName[i] + "(" + petGenre[i] + ")")
        print("   " + "Raza:  " + petKind[i])
        nombre = averiguarNom(petOwner[i])
        print("   " + "Dueño: " + petOwner[i] + " - " + nombre)
        print("")

    print("")
    print("")
    ok = False
    while ok == False:
        aux = input("Introduce el número de la mascota a borrar: ")
        num = int(aux)
        if num < leido:
            ok = True
    print("")
    print("")
    print("   ---¿Estás seguro de que quieres eliminar a esta mascota?---   ")
    o = str(num)
    print(o + ". " + petName[num] + "(" + petGenre[num] + ")")
    print("   " + "Raza:  " + petKind[num])
    nombre = averiguarNom(petOwner[num])
    print("   " + "Dueño: " + petOwner[num] + " - " + nombre)
    print("")

    ok = False
    while ok == False:
        resp = input("S/N: ")
        if resp.upper() == "S":
            numero = devnum(petOwner[num])
            del (petName[num])
            del (petOwner[num])
            del (petKind[num])
            del (petGenre[num])
            clientPet[numero] = clientPet[numero] - 1
            print("")
            savemasc()
            print("   ---Borrada correctamente---   ")
            print("")
            ok = True
        elif resp.upper() == "N":
            ook = False
            while ook == False:
                print("---¿Quieres volver a la baja (B) o al menú de mascotas (M)?---")
                print("")
                resp = input("Introduzca B o M: ")
                if resp.upper() == "B":
                    bajamasc()
                    ook = True
                elif resp.upper() == "M":
                    mascotas()
                    ook = True
        ok = True

    ook = False

    while ook == False:
        print("---¿Quieres volver al menú de mascotas (M) o al principal (P)?---")
        print("")
        resp = input("Introduzca M o P: ")
        if resp.upper() == "M":
            mascotas()
            ook = True
        elif resp.upper() == "P":
            main()
            ook = True


def altamasc():
    print_menus.altamasc()
    print("")
    print("   ---Por favor, introduzca poco a poco los datos---   ")
    print("")

    ok = False

    while ok == False:
        dni = input("Introduzca el DNI del dueño: ")
        if dni.upper() in clientID:
            ok = True

    nom = input("Introduzca el nombre de la mascota: ")
    kind = input("Introduzca la raza: ")
    genre = input("Introduzca su sexo (H o M): ")

    # posición del dni del cliente
    leido = len(clientID)
    ok = False
    pos = 0
    i = 0
    while i < leido and ok == False:
        if dni.upper() == clientID[i].upper():
            pos = i
            ok = True
        i = i + 1

    # numero de mascotas anteriores a mí
    cont = 0
    for i in range(0, pos):
        cont = cont + clientPet[i]

    # númmero de mascotas antes de mí contando las mías
    pos = cont + clientPet[pos]

    # mover todas las mascotas posteriores a mí una posición más adelante
    numero = devnum(dni)
    clientPet[numero] = clientPet[numero] + 1
    petName.append(nom)
    petOwner.append(dni)
    petKind.append(kind)
    petGenre.append(genre)

    tamani = len(petName)

    for i in range(tamani - 1, pos, -1):
        aux = petName[i - 1]
        petName[i - 1] = petName[i]
        petName[i] = aux

        aux = petOwner[i - 1]
        petOwner[i - 1] = petOwner[i]
        petOwner[i] = aux

        aux = petKind[i - 1]
        petKind[i - 1] = petKind[i]
        petKind[i] = aux

        aux = petGenre[i - 1]
        petGenre[i - 1] = petGenre[i]
        petGenre[i] = aux

    savemasc()

    ook = False
    while ook == False:
        print("")
        print("---¿Quieres volver al menú de mascotas (M) o al principal (P)?---")
        print("")
        resp = input("Introduzca M o P: ")
        if resp.upper() == "M":
            mascotas()
            ook = True
        elif resp.upper() == "P":
            main()
            ook = True


def altaclien():
    print_menus.altaclien()
    print("")
    print("   ---Por favor, introduzca poco a poco los datos---   ")
    print("")
    nom = input("Introduzca (solamente) su nombre: ")
    sur = input("Introduzca sus apellidos: ")

    ok = False

    while ok == False:
        tel = input("Introduzca su teléfono: ")
        okis = utilities.checkphone(tel)
        if okis == True:
            ok = True

    ok = False

    while ok == False:
        DNI = input("Introduzca su DNI: ")
        okis = utilities.checkID(DNI)
        if okis == True:
            ok = True

    clientName.append(nom)
    clientSurname.append(sur)
    clientPhone.append(tel)
    clientID.append(DNI)
    clientPet.append(0)
    saveclien()

    print("")
    print("   ---Añadido/a corréctamente---   ")

    print("")
    print("")

    ook = False
    while ook == False:
        print("---¿Quieres volver al menú de clientes (C) o al principal (P)?---")
        print("")
        resp = input("Introduzca C o P: ")
        if resp.upper() == "C":
            clientes()
            ook = True
        elif resp.upper() == "P":
            main()
            ook = True


def bajaclien():
    print_menus.bajaclien()

    ok = False

    while ok == False:
        DNI = input("Introduzca el DNI de la persona a borrar: ")
        okis = utilities.checkID(DNI)
        if okis == True and DNI in clientID:
            ok = True

    ok = False
    leido = len(clientID)
    i = 0

    while ok == False and i < leido:
        if clientID[i] == DNI:

            print("   ---¿Estás seguro de que quieres borrar a este cliente?---   ")

            o = str(i)
            print(o + "." + " " + clientName[i] + " " + clientSurname[i])
            print("   " + "DNI:      " + clientID[i])
            print("   " + "Teléfono: " + clientPhone[i])
            print("")
            ok = True
        else:
            i = i + 1

    ok = False

    while ok == False:
        resp = input("S/N: ")

        if resp.upper() == "S":

            del (clientName[i])
            del (clientSurname[i])
            del (clientPhone[i])
            del (clientID[i])

            saveclien()

            print("")
            print("   ---Borrado/a corréctamente---   ")

            print("")
            print("")

            ook = False

            while ook == False:
                print("---¿Quieres volver al menú de clientes (C) o al principal (P)?---")
                print("")
                resp = input("Introduzca C o P: ")
                if resp.upper() == "C":
                    clientes()
                    ook = True
                elif resp.upper() == "P":
                    main()
                    ook = True
        elif resp.upper() == "N":
            ook = False

            while ook == False:
                print("---¿Quieres volver a la baja (B) o al menú de clientes (C)?---")
                print("")
                resp = input("Introduzca B o C: ")
                if resp.upper() == "B":
                    bajaclien()
                    ook = True
                elif resp.upper() == "C":
                    clientes()
                    ook = True
        ok = True


def buscanom():
    print("")
    nom = input("Introduzca el nombre a buscar: ")
    print("")

    leido = len(clientID)
    cont = 0

    for i in range(0, leido):
        if nom.upper() in clientName[i].upper():
            print("")
            o = str(i)
            print(o + ". " + clientName[i] + " " + clientSurname[i])
            print("   " + "DNI:      " + clientID[i])
            print("   " + "Teléfono: " + clientPhone[i])
            print("")
            cont = cont + 1
    if cont == 0:
        print("   ---No existen usuarios con ese nombre---   ")

    ook = False
    while ook == False:
        print("")
        print("---¿Quieres volver al menú de clientes (C) o al principal (P)?---")
        print("")
        resp = input("Introduzca C o P: ")
        if resp.upper() == "C":
            clientes()
            ook = True
        elif resp.upper() == "P":
            main()
            ook = True


def buscatel():
    print("")
    ok = False

    while ok == False:
        tel = input("Introduzca el teléfono a buscar: ")
        okis = utilities.checkphone(tel)
        if okis == True:
            ok = True

    print("")

    leido = len(clientID)
    i = 0
    ok = False

    while i < leido and ok == False:
        if tel in clientPhone[i]:
            print("")
            o = str(i)
            print(o + ". " + clientName[i] + " " + clientSurname[i])
            print("   " + "DNI:      " + clientID[i])
            print("   " + "Teléfono: " + clientPhone[i])
            print("")
            ok = True
        else:
            i = i + 1
    if ok == False:
        print("   ---No existen usuarios con ese teléfono---   ")

    ook = False
    while ook == False:
        print("")
        print("---¿Quieres volver al menú de clientes (C) o al principal (P)?---")
        print("")
        resp = input("Introduzca C o P: ")
        if resp.upper() == "C":
            clientes()
            ook = True
        elif resp.upper() == "P":
            main()
            ook = True


def buscaDNI():
    print("")

    ok = False

    while ok == False:
        DNI = input("Introduzca DNI a buscar: ")
        okis = utilities.checkID(DNI)
        if okis == True:
            ok = True

    print("")

    leido = len(clientID)
    i = 0
    ok = False

    while i < leido and ok == False:
        if DNI.upper() in clientID[i]:
            print("")
            o = str(i)
            print(o + ". " + clientName[i] + " " + clientSurname[i])
            print("   " + "DNI:      " + clientID[i])
            print("   " + "Teléfono: " + clientPhone[i])
            print("")
            ok = True
        else:
            i = i + 1
    if ok == False:
        print("   ---No existen usuarios con ese DNI---   ")

    ook = False
    while ook == False:
        print("")
        print("---¿Quieres volver al menú de clientes (C) o al principal (P)?---")
        print("")
        resp = input("Introduzca C o P: ")
        if resp.upper() == "C":
            clientes()
            ook = True
        elif resp.upper() == "P":
            main()
            ook = True


def buscaclien():
    print_menus.buscaclien()
    print("")
    print("   ---Introduzca modo de busqueda---   ")
    print("")

    ok = False

    while ok == False:
        resp = input("Número: ")
        if resp == "1":
            buscanom()
            ok = True
        elif resp == "2":
            buscaDNI()
            ok = True
        elif resp == "3":
            buscatel()
            ok = True
        elif resp == "9":
            clientes()
            ok = True


def mostrarclientes():
    leido = len(clientID)

    print("")

    for i in range(0, leido):
        o = str(i)
        print(o + ". " + clientName[i] + " " + clientSurname[i])
        print("   " + "DNI:      " + clientID[i])
        print("   " + "Teléfono: " + clientPhone[i])
        devmasc(i)
        print("")


def clientes():
    print_menus.menuclien()

    ok = False
    while ok == False:

        num = input("Introduzca número: ")

        if num == "1":
            mostrarclientes()
            ook = False
            while ook == False:
                print("---¿Quieres volver al menú de clientes (C) o al principal (P)?---")
                print("")
                resp = input("Introduzca C o P: ")
                if resp.upper() == "C":
                    clientes()
                    ook = True
                elif resp.upper() == "P":
                    main()
                    ook = True
            ok = True
        elif num == "2":
            altaclien()
            ok = True
        elif num == "3":
            bajaclien()
            ok = True
        elif num == "4":
            editclien()
            ok = True
        elif num == "5":
            buscaclien()
            ok = True
        elif num == "9":
            main()


refresh()

main()
