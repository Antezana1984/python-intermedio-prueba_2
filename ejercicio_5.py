def imprimir_mi_tupla(*args):
    print("Recibe un parámetro tipo : " + str(type(args)))

    for i in range(len(args)):
        print(args[i])
        print("\n")    #Debería imprimir cada elemnto por separado y un salto de línea pero no resultó

        
def main():

    # Se crea lista con colores favoritos
    lista = []
    while  True: 
        color = input("Ingrese tu color favorito (cuando quieras salir, escribe salir): ")
        color = color.upper()
        if color == "SALIR":
            break
        lista.append(color)   


    # Transforma la lista en tupla
    mi_tupla = tuple(lista)

    # Imprime la tupla empleando *args
    imprimir_mi_tupla(mi_tupla)




if __name__ == "__main__":
    main()