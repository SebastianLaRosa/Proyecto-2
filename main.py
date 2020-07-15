while True:
    print("Si desea registrarse, ingrese 1, si desea hacer una compra anonima, ingrese 2: ")
    x = int(input("Ingrese una opcion: "))
    print("")
    if x == 1:
        print("Si es su primera compra, ingrese 1, si ya esta registrado ingrese 2")
        r = int(input("Ingrese una opcion: "))
        print("")
        if r == 1:
            n = str(input("Ingrese su nombre: "))
            write = open('Cuentas.txt', 'a')
            write.write(n)
            write.write("\n")
            write.close()
        if r == 2:
            n = input("Ingrese su nombre: ")
            read = open('Cuentas.txt', 'r')
            for line in read.readlines():
                if n == line:
                    p = True
                    break
                else:
                    p = False
                    print("Su nombre no ha sido encontrado, por favor, ingrese un nombre de alguien que ya haya realizado una compra")

        break


'''from Admin import buscar_productos
from Admin import lugares
from Admin import productos
from Admin import carrito_compras
from Admin import carrito
from Admin import pago
from Admin import monto_pagar

print("")
while True:
#Este es el primer menu que el usuario encuentra
    print("Menu Principal")
    print("1. Buscar Producto")
    print("2. Ver Carrito de Compras")
    print("3. Pagar")
    print("4. Salir")
    opcion = int(input("Ingrese la opcion : "))
    print("\n")
    if 1 <= opcion <= 4:
        if opcion == 1:
            #A traves de esta interfaz el cliente es capaz de encontrar sus productos
            buscar_productos(lugares, productos)
        elif opcion == 2:
            #Esta funcion permite que el usuario tenga conocimiento de la inversion que va a realizar
            carrito(carrito_compras, monto_pagar)
        elif opcion == 3:
            #Con este codigo el usuario podra ingresar sus datos para realizar el pago
            pago()
            break
        elif opcion == 4:
            #Si el cliente lo desea, podra retractarse de realizar una compra con esta parte del programa
            salir = str(input("¿Usted desea salir?, recuerde que no se guardarán los elementos de su carrito de compras: "))
            if salir.lower() == "si":
                break
            print("\n")'''