from functools import reduce

def llenar_lista():

    # Se probó con la lista [2, 3, 4, 5, 6]
    
    lista = []
    # Llena la lista, se detiente cuando el usuario ingresa un cero
    valor = int(input("Ingresar valor (0 para finalizar):"))
    
    while valor != 0:
        lista.append(valor)    
        valor=int(input("Ingresar valor (0 para finalizar):"))

    return lista
    

def main():

    Lista = []
    lista = llenar_lista()

    bienvenida = """
    Bienvenido al Menú
      1) Suma
      2) Resta
      3) Multiplicación
      4) División
      5) Exponenciación
      6) Raíz 
    Elija una opción: """

    opcion = int(input(bienvenida))

    if opcion == 1:
        producto = reduce(lambda a, b: a + b, lista)
        print(producto)
    elif opcion == 2:
        producto = reduce(lambda a, b: a - b, lista)
        print(producto)
    elif opcion == 3:
        producto = reduce(lambda a, b: a * b, lista)
        print(producto)
    elif opcion == 4:
        producto = reduce(lambda a, b: a / b, lista) 
        print(producto)
    elif opcion == 5:
        producto = reduce(lambda a, b: a ** b, lista)
        print(producto)
    elif opcion == 6:
        producto = reduce(lambda a, b: (a ** (1/b)), lista)
        print(producto)
    else: 
        print("No es opción válida")



if __name__ == "__main__":
    main()