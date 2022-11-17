from functools import reduce


def llena_las_listas():

    lista = []
    ingreso = 0.0
    for nota in range(6):
        ingreso = float(input("Ingrese a nota: "))
        lista.append(ingreso)

    return lista


def main():

    # Crea las listas

    Pedro = []
    Juan = []
    María = []
    lista_con_los_promedios_finales = []

    # Llena las listas con las 6 notas empleando funciones

    Pedro = llena_las_listas()
    Juan = llena_las_listas()
    María = llena_las_listas()

    for i in range(6):                  
        lista_auxiliar = []             #lista que toma las tres notas de cada alumno para promediarlas
        promedio = 0                    #promedio de cada asignatura

        lista_auxiliar.insert(0, Pedro[i])  #toma las notas de cada asignatura y las lleva a una lista auxiliar
        lista_auxiliar.insert(1, Juan[i])
        lista_auxiliar.insert(2, María[i])
        
        promedio =   ( reduce(lambda a, b: a + b, lista_auxiliar) / 3 )  #calcula promedio empleando "reduce"
        
        lista_con_los_promedios_finales.append(promedio) 
        
    
    print("Los promedios finales son los siguientes: ")
    print("Historia  : " + str(round(lista_con_los_promedios_finales[0], 2) ))
    print("Lenguaje  : " + str(round(lista_con_los_promedios_finales[1], 2) ))
    print("Matemática: " + str(round(lista_con_los_promedios_finales[2], 2) ))
    print("Física    : " + str(round(lista_con_los_promedios_finales[3], 2) ))
    print("Química   : " + str(round(lista_con_los_promedios_finales[4], 2) ))
    print("Biología  : " + str(round(lista_con_los_promedios_finales[5], 2) ))
   

if __name__ == "__main__":
    main()
    