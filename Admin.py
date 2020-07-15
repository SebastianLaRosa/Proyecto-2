lugares = ["Estudio", "Sala", "Cocina", "Baño", "Lavandería"]
productos = [
    {"nombre": "Monitor", "precio": 2700, 'lugar': "Estudio"},
    {"nombre": "Aire acondicionado", "precio": 700, 'lugar': "Estudio"},
    {"nombre": "Headset", "precio": 620, 'lugar': "Estudio"},
    {"nombre": "Teclado", "precio": 480, 'lugar': "Estudio"},
    {"nombre": "Televisor", "precio": 2700, 'lugar': "Sala"},
    {"nombre": "Parlantes", "precio": 300, 'lugar': "Sala"},
    {"nombre": "Router", "precio": 200, 'lugar': "Sala"},
    {"nombre": "Horno c/ cocina", "precio": 1000, 'lugar': "Cocina"},
    {"nombre": "Refrigeradora", "precio": 2000, 'lugar': "Cocina"},
    {"nombre": "Licuadora", "precio": 400, 'lugar': "Cocina"},
    {"nombre": "Tostadora", "precio": 100, 'lugar': "Cocina"},
    {"nombre": "Secadora de pelo", "precio": 200, 'lugar': "Baño"},
    {"nombre": "Maquina de afeitar", "precio": 200, 'lugar': "Baño"},
    {"nombre": "Balanza", "precio": 150, 'lugar': "Baño"},
    {"nombre": "Lavadora", "precio": 1700, 'lugar': "Lavanderia"},
    {"nombre": "Secadora", "precio": 2700, 'lugar': "Lavanderia"},
    {"nombre": "Terma", "precio": 2700, 'lugar': "Lavanderia"},
]
carrito_compras = []
monto_pagar = 0

import csv


def buscar_productos(lugares, productos):
    print("Lugares")
    if len(lugares) > 0:
        while True:
            for i in range(len(lugares)):
                print(i+1, ". ", lugares[i])
            opcion_lugar = int(input("Ingrese la opcion del lugar : "))
            if 1 <= opcion_lugar <= len(lugares):
                lista_productos_encontrados = []
                for j in range(len(productos)):
                    if productos[j]['lugar'] == lugares[opcion_lugar-1]:
                        lista_productos_encontrados.append(productos[j])
                if len(lista_productos_encontrados) == 0:
                    print("Productos no Encontrados")
                else:
                    while True:
                        print("Se encontraron ", len(lista_productos_encontrados), " productos")
                        v = 0
                        v_2 = 7
                        for w in range(len(lista_productos_encontrados)):
                            if len(lista_productos_encontrados[w]['nombre']) - 7 > v:
                                v = len(lista_productos_encontrados[w]['nombre']) - 7
                            if len(lista_productos_encontrados[w]['nombre']) > v_2:
                                v_2 = len(lista_productos_encontrados[w]['nombre'])
                        print("Producto", " "*5, "Nombre", " " *v, "Precio", " "*7,"Cantidad")
                        print("")
                        for z in range(len(lista_productos_encontrados)):
                            with open('Cuentas.csv', 'r') as file:
                                reader = csv.reader(file)
                                next(file)
                                for line in reader:
                                    if line[0] == lista_productos_encontrados[z]['nombre']:
                                        x = line[1]
                            print(" "*3, z+1, "\t", lista_productos_encontrados[z]['nombre'], " "*(v_2-len(lista_productos_encontrados[z]['nombre'])), "\t",lista_productos_encontrados[z]['precio']," "*v, x)
                            print("")

                        print("Si desea salir, ingrese '0'")
                        opcion_productos = int(input("Ingrese que productos desea agregar al carrito : "))
                        if 1 <= opcion_productos <= len(lista_productos_encontrados):
                            carrito_compras.append(lista_productos_encontrados[opcion_productos-1])
                        if opcion_productos == 0:
                            print("\n")
                            break
            break


def carrito(carrito_compras, monto_pagar):
    print("Existe(n) ", len(carrito_compras), " producto(s)")
    for i in range(len(carrito_compras)):
        print("Producto", i+1)
        print("Nombre del Producto : ", carrito_compras[i]['nombre'])
        print("Precio del Producto : ", carrito_compras[i]['precio'])
        print()
    for x in range(len(carrito_compras)):
        monto_pagar += int(carrito_compras[x]["precio"])
    print("El monto a pagar es " + str(monto_pagar) + " soles")
    print("\n")

def pago():
    tarjeta = str(input("Ingrese su numero de tarjeta: "))
    while True:
        if 13 > len(tarjeta) or len(tarjeta) > 18:
            tarjeta = str(input("Por favor, ingrese un numero válido: "))
        else:
            break
    print("Si desea que enviemos sus productos a alguna direccion, ingrese la opcion 1")
    print("Si desea recojer en tienda, ingrese la opcion 2")
    n = int(input("Ingrese una opcion: "))
    while True:
        if n == 1:
            direccion = input("Ingrese una direccion: ")
            print("Su compra ha sido procesada, gracias por elegirnos")
            break
        elif n == 2:
            print("Nuestras tiendas no estan disponibles por el momento")
            n = int(input("Elija otra opcion: "))

