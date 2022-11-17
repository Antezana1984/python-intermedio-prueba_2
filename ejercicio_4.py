# Resuelva los siguientes bloques de código añadiendo las sentencias Try/Except que
# considere necesarias. Si el bloque de código no tiene errores, imprima "El bloque de 
# código no tiene errores" en la consola y el resultado del bloque según corresponda. 
# Si el bloque de código tiene errores, imprima el error en la consola.

def bloque_1():
    try:
        mi_lista = ["Python","C","C++","JavaScript"]
        print(mi_lista[5])
    except IndexError as Error:
        print("índice fuera de rango, surge si se accedes a índices no válidos en tu lista")
        print(Error)
    else:
        print("El bloque try se ejecutó sin errores")
    finally:
        print("Se terminó de ejecutar el bloque_1")

def bloque_2(num):
    try:
        resultado = num + 10
        print(resultado)
    except TypeError as Error:
        print("Error de tipo: usaste un tipo de dato incorrecto")
        print(Error)
    else:
        print("El bloque try se ejecutó sin errores")
    finally:
        print("Se terminó de ejecutar el bloque_2")

def bloque_3():
    try:
        capitales  = {
            "Colombia": "Bogotá",
            "Argentina": "Buenos Aires",
            "Perú": "Lima",
            "Chile": "Santiago de Chile",
        }
        print(capitales["Brasil"])
    except KeyError as Error:
        print("Puede ser error de parámetros en la función")
        print(Error)
    else:
        print("El bloque try se ejecutó sin errores")
    finally:
        print("Se terminó de ejecutar el bloque_3")
        

def main():
    print("Bloque 3")
    bloque_3()
    print("-------------")


if __name__ == '__main__':
    main()