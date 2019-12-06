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

clientName = ["Manuel","Vanesa","David","Pablo","Pablo"]
clientSurname = ["Carrasco","Martín","Bisbal","Alborán","López"]
clientID = ["00000000M","00000000V","00000000D","00000000P","00000001P"]
clientPhone = ["111111111","222222222","333333333","444444444","555555555"]

def main():
    print_menus.principalmenu()

    ok = False
    while ok == False:

        num = input("Introduzca número: ")

        if num == "1":
            #funcion horario hoy
            ok = True
        elif num == "2":
            #funcion calendario
            ok = True
        elif num == "3":
            #funcion citas
            ok = True
        elif num == "4":
            clientes()
            ok = True
        elif num == "5":
            #funcion mascotas
            ok = True
        elif num == "9":
            exit(9)

def altaclien():
    print_menus.altaclien()
    print("")
    print("   ---Por favor, introduzca poco a poco los datos---   ")
    print("")
    nom = input("Introduzca (solamente) su nombre: ")
    sur = input("Introduzca sus apellidos: ")
    tel = input("Introduzca su teléfono: ")
    dni = input("Introduzca su DNI: ")

    clientName.append(nom)
    clientSurname.append(sur)
    clientPhone.append(tel)
    clientID.append(dni)

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
    return True

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
    tel = input("Introduzca el teléfono a buscar: ")
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
    DNI = input("Introduzca DNI a buscar: ")
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
            #mostrar clientes
            leido = len(clientID)

            print("")

            for i in range(0, leido):
                if i == 0:
                    print("1. "+clientName[i]+" "+clientSurname[i])
                    print("   "+"DNI:      "+clientID[i])
                    print("   "+"Teléfono: "+clientPhone[i])
                    print("")
                else:
                    o = str(i+1)
                    print(o+". "+clientName[i]+" "+clientSurname[i])
                    print("   "+"DNI:      "+clientID[i])
                    print("   "+"Teléfono: "+clientPhone[i])
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