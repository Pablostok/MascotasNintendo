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

clientName = ["Manuel","Vanesa","David"]
clientSurname = ["Carrasco","Martín","Bisbal"]
clientID = ["00000000M","00000000V","00000000D"]
clientPhone = ["111111111","222222222","333333333"]

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

def buscaclien():
    return True


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