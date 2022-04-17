#Asignación

CLAVE_USUARIO = "1313"                  #Clave del usuario
LISTA_RETIROS = [20,50,100,150,500]     #Lista con las cantidades de retiro predeterminadas
saldo = 10000                           #Saldo disponible

#Autentificación de clave

while True:

    clave = input("Ingrese su clave de 4 dígitos: ")

    if clave == CLAVE_USUARIO:
        print("\n¡Clave correcta!")
        break

    else:
        print("\nClave incorrecta")

#Bucle para las operaciones

while True:

    #Menu para el usuario

    print("\n--------------MENÚ PRINCIPAL--------------")
    print("Puede realizar las siguientes operaciones:\n1.Retirar fondos\n2.Visualizar saldo\n3.Salir")
    seleccion = input("\nIngrese el número de la operación que desea realizar: ")

    if seleccion != "1" and seleccion != "2" and seleccion != "3":
        print("\n¡Valor ingresado inválido. Por favor ingrese un número que se encuentre dentro de las opciones brindadas!")
        continue

    #Operación retirar saldo

    elif seleccion == "1":

        if saldo == 0:
            print("\nLo sentimos, no puede realizar retiros si su saldo es de S/0")
            continue
        
        while True:

            print("\nPuede retirar las siguientes cantidades:\n1.S/20\n2.S/50\n3.S/100\n4.S/150\n5.S/500\n6.Ingresar monto")

            try:
                seleccion = int(input("\nIngrese el número de la cantidad que desea retirar: "))
                
            except ValueError:
                print("\n¡Valor ingresado inválido. Por favor ingrese un número que se encuentre dentro de las opciones brindadas!")
                continue

            #Si el usuario desea una cantidad predeterminada
            if seleccion > 0 and seleccion < 6:
                    #Asignamos la cantidad deseada basada en el índice en LISTA_RETIROS
                    cantidad_deseada = LISTA_RETIROS[seleccion-1]

            #Si el ususario desea retirar otra cantidad
            elif seleccion == 6:

                while True:

                    try:
                        cantidad_deseada = int(input("\nIngrese la cantidad que desea retirar: "))

                    except ValueError:

                        print("\n¡Valor ingresado inválido. Por favor ingrese un valor numérico!")
                        continue

                    #La cantidad deseada no puede ser igual a 0
                    if cantidad_deseada <= 0:
                        print("\nPor favor, ingrese un valor diferente y mayor a 0")
                        continue

                    break
                        
            else:
                print("\n¡Valor ingresado inválido. Por favor ingrese un número que se encuentre dentro de las opciones brindadas!")
                continue

            #La cantidad deseada no puede ser mayor al saldo disponible
            if cantidad_deseada > saldo:

                print("\nLa cantidad ingresada es mayor a su saldo actual(S/{}). Ingrese otra cantidad.".format(saldo))
                continue

            else:
                #Se sustrae la cantidad deseada del saldo
                saldo -= cantidad_deseada
                while True:
                    #Se le da la opción al usuario de visualizar su saldo restante
                    seleccion = input("\n¡Retiro exitoso!, ¿Desea visualizar su saldo actual?:\n1.Sí\n2.No\nIngrese su selección: ")
                    if seleccion == "1":
                        print("\nSu saldo actual es de: S/{}".format(saldo))
                        break
                    elif seleccion == "2":
                        print("\nSerá redirigido al menú principal....")
                        break
                    else:
                        print("\n¡Valor ingresado inválido. Por favor ingrese un número que se encuentre dentro de las opciones brindadas!")

            break

    #Operación visualizar saldo

    elif seleccion == "2":
        print("\nSu saldo actual es de: S/{}".format(saldo))
    
    #Si el usuario decide salir del menú
    
    else:
        print("\n¡Hasta luego!\n")
        break

                






