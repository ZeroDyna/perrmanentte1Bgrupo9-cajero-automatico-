# Cajero automático
Este programa fue elaborado con la intención de simular ciertas funciones de un cajero automático como retirar dinero y observar el saldo disponible.

Este programa es parte del desarrollo del curso Programación de Videojuegos de la carrera Ciencias de la Computación de la UCSP.

Por los alumnos:
- Renato Corrales Peña
- Alexis Espinoza Villanueva

## Instrucciones de ejecución
1. El ususario deberá tener instalado python e ingresar

    ```
    >>> python3 .py
    ```

2. Al iniciar el programa se le pedira al usuario que ingrese su clave de 4 dígitos.

    ```
    Ingrese su clave de 4 dígitos: 
    ```

3. El usuario deberá ingresar la clave 1313 para poder acceder al menú pricipal donde el usuario podra elegir entre 3 opciones: 1. Retirar fondos, 2.Visualizar saldo, 3.Salir.

    ```
    --------------MENÚ PRINCIPAL--------------
    Puede realizar las siguientes operaciones:
    1.Retirar Fondos
    2.Visualizar Saldo
    3.Salir

    Ingrese el número de la operación que desea realizar: 
    ```
4. Si el usuario decide retirar fondos, es redirigido a un menú donde podrá elegir un monto predeterminado o ingresar un monto específico.

    ```
   Puede retirar las siguientes cantidades:
    1.S/20
    2.S/50
    3.S/100
    4.S/150
    5.S/500
    6.Ingresar monto

    Ingrese el número de la cantidad que desea retirar:
    ```

    1. En caso el usuario seleccione la sexta opción, deberá ingresar la cantidad de dinero que desea retirar.

        ```
       Ingrese la cantidad que desea retirar:
        ```
    
    2. La cantidad seleccionada o ingresada por el usuario es luego sustraida de su saldo actual y luego se le preguntará si quiere visualizar su saldo después de realizar la operación.

        ```
        ¡Retiro exitoso!, ¿Desea visualizar su saldo actual?:
        1.Sí
        2.No
        Ingrese su selección:
        ```
    
    3. Luego el usuario será redirigido al menú prinicpal.

5. Si el usuario decide visualizar su saldo, se le mostrará un mensaje indicando su saldo actual.

    ```
    Su saldo actual es de: S/10000
    ```

6. En caso el usuario decida salir, se le mostrará un mensaje de despedida y el programa finalizará.

    ```
    ¡Hasta luego!
    ```

## Posibles mensajes de error

- Si el usuario ingresa un valor fuera de las opciones brindadas por el programa, se le mostrar uno de los siguientes mensajes:

    ```
    ¡Valor ingresado inválido. Por favor ingrese un número que se encuentre dentro de las opciones brindadas!
    ```

- Si el usuario no cuenta con fondos en su cuenta e intenta realizar un retiro, se le mostrará el siguiente mensaje:

    ```
    Lo sentimos, no puede realizar retiros si su saldo es de S/0
    ```
- Si el usuario intenta retirar una cantidad mayor a su saldo actual, se le mostrará un mensaje como el siguiente:

    ```
    La cantidad ingresada es mayor a su saldo actual(S/10000). Ingrese otra cantidad.
    ```
- Si el usuario al momento de especificar la cantidad que desea retirar ingresa un valor no numérico, se le mostrará el siguiente mensaeje:

    ```
    ¡Valor ingresado inválido. Por favor ingrese un valor numérico!
    ```
- Si el usario al momento de especificar la cantidad que desea retirar ingresa un número negativo o 0, se le mostrará el siguiente mensaje:

    ```
    Por favor, ingrese un valor diferente y mayor a 0
    ```

