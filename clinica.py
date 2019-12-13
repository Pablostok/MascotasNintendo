import print_menus
import utilities


def copyright():
    print("###############################################################")
    print("#                                                             #")
    print("#                  CLÍNICA VETERINARIA                        #")
    print("#                ---Mascotas Nintendo---                      #")
    print("#                                                             #")
    print("#                                 Amanda G.P. & Pablo V.R.    #")
    print("###############################################################")


#########################################################################################
clientName = ["Manuel", "Vanesa", "David", "Pablo", "Pablo"]
clientSurname = ["Carrasco", "Martín", "Bisbal", "Alborán", "López"]
clientID = ["00000000M", "00000000V", "00000000D", "00000000P", "00000001P"]
clientPhone = ["111111111", "222222222", "333333333", "444444444", "555555555"]
#########################################################################################
clientPet = [1, 3, 0, 1, 1]
petOwner = ["00000000M", "00000000V", "00000000V", "00000000V", "00000000P", "00000001P"]
petName = ["Toad", "Pikachu", "Furret", "Yoshi", "Luigi", "Bulbasur"]
petKind = ["Perro", "Hamster", "Hurón", "Perro", "Pato", "Tortuga"]
petGenre = ["H", "M", "H", "M", "M", "H"]


#########################################################################################

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
            exit(9)


def devmasc(numclien):
    nummasc = clientPet[numclien]
    leido = len(clientID)
    # Hasta aquí bien

    if numclien == 0:
        posanterior = clientPet[0]
    else:
        posanterior = clientPet[numclien-1]

    if nummasc == 0:
        return True
    else:
        for i in range(posanterior, nummasc):
            o = str(i)
            print("   " + "Pet " + o + ": " + petName[i] + " - " + petKind[i] + "(" + petGenre[i] + ")")


def mascotas():
    print_menus.menumasc()
    ok = False
    while ok == False:
        num = input("Introduzca número: ")

        if num == "1":
            # mostrar mascotas
            ok = True
        elif num == "2":
            altamasc()
            ok = True


def altamasc():
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
    genre = input("Introduzca su sexo: ")

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

    # númmero de mascotas después de mí contando las mías
    cont = cont + clientPet[pos]

    # mover todas las mascotas posteriores a mí una posición más adelante
    petName.append(nom)


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
            print(o + "." +" " + clientName[i] + " " + clientSurname[i])
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

            del(clientName[i])
            del(clientSurname[i])
            del(clientPhone[i])
            del(clientID[i])

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


def clientes():
    print_menus.menuclien()

    ok = False
    while ok == False:

        num = input("Introduzca número: ")

        if num == "1":
            # mostrar clientes
            leido = len(clientID)

            print("")

            for i in range(0, leido):
                if i == 0:
                    print("1. " + clientName[i] + " " + clientSurname[i])
                    print("   " + "DNI:      " + clientID[i])
                    print("   " + "Teléfono: " + clientPhone[i])
                    devmasc(i)
                    print("")
                else:
                    o = str(i + 1)
                    print(o + ". " + clientName[i] + " " + clientSurname[i])
                    print("   " + "DNI:      " + clientID[i])
                    print("   " + "Teléfono: " + clientPhone[i])
                    devmasc(i)
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
            ok = True
        elif num == "2":
            altaclien()
            ok = True
        elif num == "3":
            bajaclien()
            ok = True
        elif num == "4":
            buscaclien()
            ok = True
        elif num == "9":
            main()


main()
