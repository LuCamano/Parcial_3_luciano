from os import system
system('cls')

#Listas
tipo = []
destinatario = []
rutDestinatario = []
peso = []
precio = []
ciudadDestino = []

#Definir funciones
def Ingresar():
    agregado = False
    while True:
        try:
            tipof = str(input('Ingrese tipo de encomienda: '))
            tipof.upper()
            if tipof == 'sobre' or tipof == 'paquete':
                tipo.append(tipof)
                break
            else:
                print('Tipo incorrecto, la encomienda debe ser sobre o paquete')
        except:
            print('Error de entrada')
    while True:
        try:
            nombreDestin = str(input('Nombre del Destinatario: '))
            nombreDestin.upper()
            if len(nombreDestin) >= 2 and len(nombreDestin) <= 30:
                destinatario.append(nombreDestin)
                break
            else:
                print('El nombre debe contener entre 2 y 30 caracteres.')
        except:
            print('Error de entrada')
    while True:
        try:
            rut = str(input('Ingrese el rut del destinatario: '))
            rut.upper()
            guion = rut.find('-')
            if guion != -1:
                rutDestinatario.append(rut)
                break
            else:
                print('El rut debe contener guion.')
        except:
            print('Error de entrada')
    while True:
        try:
            ingrPeso = float(input('Ingrese peso de la encomienda: '))
            if ingrPeso >= 0.1:
                peso.append(ingrPeso)
                break
            else:
                print('Peso no valido.')
        except:
            print('Error de entrada')
    while True:
        try:
            ingrPrecio = int(input('Precio: '))
            if ingrPrecio >= 2000:
                precio.append(ingrPrecio)
                break
            else:
                print('El precio debe ser mayor a $2.000')
        except:
            print('Error de entrada')
    while True:
        try:
            ciudad = str(input('Ingrese ciudad de destino: '))
            ciudad.upper()
            if len(ciudad) >= 3:
                ciudadDestino.append(ciudad)
                agregado = True
                break
            else:
                print('Debe contener más de 3 caracteres.')
        except:
            print('Error de entrada')

    if agregado:
        print(' TIPO    | DESTINATARIO         | RUT        | PESO (KG) | PRECIO   | CIUDAD DESTINO                ')
        print(f' {tipof} | {nombreDestin} | {rut} | {ingrPeso} | {ingrPrecio} | {ciudad}')


#Main

while True:
    try:
        opt=int(input('Caracol Express\nBienvenido/a!\n\n¿Qué operación desea realizar?\n1.Ingresar encomienda\n2.Buscar encomienda\n3.Listar encomiendas\n0.Salir\n>'))
        if opt == 0:
            break
        elif opt == 1:
            Ingresar()
        elif opt == 2:
            print('No lo alcance a hacer')
        elif opt == 3:
            print('No lo alcance a hacer')
    except:
        print('Error')