import print_menus
import utilities

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
            #funcion clientes
            ok = True
        elif num == "5":
            #funcion mascotas
            ok = True
        elif num == "9":
            exit(9)


main()