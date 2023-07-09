registros = []

def grabar():
    print("BIENVENIDO AL INGRESO DE DATOS DEL SISTEMA".center(50))
    try:
        envio = {}
        rut = str(input("A.- INGRESE EL RUT DEL DESTINATARIO:\n"))
        if rut[-2] == "-":
            envio["rut"] = rut.upper()
        else:
            print('EL RUT DEBE CONTENER UN GUION "-"')
            return

        nombre = str(input("B.- INGRESE EL NOMBRE DEL DESTINATARIO:\n"))
        if len(nombre) > 2 and len(nombre) <= 30:
            envio["nombre"] = nombre.upper()
        else:
            print("EL NOMBRE DEBE SER MAYOR A 3 LETRAS Y MENOR DE 30 LETRAS")
            return

        ciudad = str(input("C.- INGRESE LA CIUDAD DEL DESTINATARIO:\n"))
        if len(ciudad) >= 3:
            envio["ciudad"] = ciudad.upper()
        else:
            print("LA CIUDAD DEBE TENER MAS DE TRES LETRAS\n")
            return

        peso = float(input("D.- INGRESE EL PESO DE SU ENVIO:\n"))
        if peso > 0.1:
            envio["peso"] = peso
        else:
            print("EL PESO DEBE SER MAYOR A 0.1\n")
            return

        precio = int(input("E.- INGRESE EL PRECIO DE SU PAQUETE (PRECIO MINIMO $2.000):\n"))
        if precio > 2000:
            envio["precio"] = precio
        else:
            print("POR FAVOR INGRESE UN PRECIO MAYOR A $2.000")
            return

        tipo_paquete = int(input("F.- INGRESE EL TIPO DE PAQUETE A ENVIAR:\n1.- PAQUETE\n2.- SOBRE\n"))
        if tipo_paquete == 1:
            envio["tipo"] = "PAQUETE"
        elif tipo_paquete == 2:
            envio["tipo"] = "SOBRE"
        else:
            print("INGRESE UNA OPCION VALIDA\n")
            return

        registros.append(envio)
        print("ENVIO REGISTRADO EXITOSAMENTE")

    except:
        print("POR FAVOR INGRESE LOS DATOS SOLICITADOS DE MANERA CORRECTA\n".center(50))

    menu()

def buscar():
    busqueda_rut = str(input("INGRESE EL RUT A BUSCAR:".center(50)))
    encontrado = False
    for envio in registros:
        if envio["rut"] == busqueda_rut:
            print("INFORMACION DEL ENVIO:")
            print(f"RUT: {envio['rut']}")
            print(f"NOMBRE: {envio['nombre']}")
            print(f"CIUDAD: {envio['ciudad']}")
            print(f"PESO ENVIO: {envio['peso']}")
            print(f"PRECIO ENVIO: {envio['precio']}")
            print(f"TIPO DE ENVIO: {envio['tipo']}")
            encontrado = True
            break

    if not encontrado:
        print("ENVIO NO ENCONTRADO")

    menu()

def listar():
    input("PRESIONE ENTER PARA LISTAR TODOS LOS ENVIOS".center(50))
    print("LISTA DE ENVIOS:")
    for envio in registros:
        print(f"RUT: {envio['rut']}")
        print(f"NOMBRE: {envio['nombre']}")
        print(f"CIUDAD: {envio['ciudad']}")
        print(f"PESO ENVIO: {envio['peso']}")
        print(f"PRECIO ENVIO: {envio['precio']}")
        print(f"TIPO DE ENVIO: {envio['tipo']}")
        print("-" * 50)

    menu()

def menu():
    while True:
        try:
            print("BIENVENIDO AL MENU".center(50))
            opc = int(input("""1.- INGRESAR DATOS DEL ENVIO\n2.- BUSQUEDA POR RUT\n3.- LISTAR TODOS LOS DATOS\n4.- SALIR\n"""))
            if opc == 1:
                grabar()
                break
            elif opc == 2:
                buscar()
                break
            elif opc == 3:
                listar()
                break
            elif opc == 4:
                print("VUELVA PRONTO!\n")
                return
        except:
            print("DIGITE UNA OPCION VALIDA")

menu()
