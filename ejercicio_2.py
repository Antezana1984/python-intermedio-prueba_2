def es_primo(numero):
   # if numero == 1:
    #    return  False
    for i in range(2, numero):
        if (numero % i) == 0:
            return False
    return True




    

def main():
    p = int(input("Ingrese un  número: "))
    print("¿Es primo? : " + str(es_primo(p)))

    lista1 = []
    lista2 = range(1, 1001)
    lista1 = list( filter(lambda numero: es_primo(numero), lista2) )
    print(lista1)


if __name__ == "__main__":
    main()
    
    