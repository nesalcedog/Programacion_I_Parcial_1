from validaciones import *


def cargar_matriz_notas(matriz:list):
    ''' 
    Esta funcion espera recibir una matriz vacia para cargar cantidades de alumnos y cantidades de examenes
    Luego se pide al usuario agregar las notas de los examenes de cada alumno
    '''
    n = int(input('Cuantos alumnos tomaron examen?: '))
    m = int(input('Cuantos examenes se tomaron?: '))    

    for i in range(n):  ##Creo la matriz de alumnos y examenes
        filas = [0] * m
        matriz += [filas]

    

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            notas = input(f'Ingrese nota del 1 al 10 del alumno {i+1} en la materia {j+1}: ')
            if type(notas) == str and notas.isdigit(): ##Valido si lo ingresado es un string con digitos
                notas_int = int(notas) #Aca lo casteo a int para poder hacer el if que sigue
                if notas_int >= 1 and notas_int <= 10: ##Valido si la nota esta entre 1 y 10
                    matriz[i][j] = notas_int #Cago la nota ingresada en el indice correspondiente
                else:
                    print('Error: Debe cargar un numero entero de 1 a 10')
                    notas = input(f'Ingrese nota del 1 al 10 del alumno {i+1} en la materia {j+1}: ')
            else:
                print('Error: Ingrese dato valido')
    print(matriz) ##Aca tendria que ir un return matriz para que funcione todo, no lo cambio porque no se puede je
    


def porcentaje_aprobados(matriz:list):
    ''' 
    Esta funcion espera recibir una matriz cargada
    y calcula el porcentaje de examenes aprobados
    '''    
    for i in range(len(matriz)):
        examenes_aprobados = 0 #Creo la variable para sumar la nota de los alumnos aprobados
        examenes_realizados = 0 #Variable de examenes totales
        for j in range(len(matriz[i])):
            examenes_realizados += 1
            if matriz[i][j] >= 6: #Solo sumo las notas aprobadas
                examenes_aprobados += 1
        
        porcentaje_aprobado = (examenes_aprobados / examenes_realizados) *100
        print(f'El porcentaje de aprobacion del alumno {i+1} es {porcentaje_aprobado} %')

def mejor_promedio(matriz:list):
    ''' 
    Calcula el promedio de cada alumno
    Determina cuál tiene el mejor promedio. 
    Retorna el alumno y el valor del promedio.
    ''' 
    alumnos = 0
    matriz_promedios = []

    for i in range(len(matriz)):
        acumulador_notas = 0 #Creo la variable acumular las notas de los examenes
        examenes_realizados = 0 #Variable de examenes totales
        for j in range(len(matriz[i])):
            examenes_realizados += 1
            acumulador_notas += matriz[i][j] #Acumulo las notas del alumno                
        promedio = (acumulador_notas / examenes_realizados) 
        matriz_promedios += [int(promedio)] #Acá pase el numero a int porque no puedo guardar float en listas
    
    mayor_promedio = float("-inf")
    for i in range(len(matriz_promedios)):
        if matriz_promedios[i] > mayor_promedio: #Busco el mayor promedio y guardo el promedio y el indice del alumno
            mayor_promedio = matriz_promedios[i]
            indice_alumno = i
    
    return (indice_alumno + 1, mayor_promedio)

def buscar_nota(matriz:list,nota_buscar:int):
    '''
    Recibe una matriz y espera que se ingrese una nota a buscar
    Devuelve la posicion de la matriz en la que se encuentra
    la nota buscada
    '''
    
    matriz_posicion = []
    posicion = 0
    if es_entero(nota_buscar):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == nota_buscar: ## Si las posiciones i y j coinciden con la nota buscada

                    matriz_posicion.append((i , j)) ##Las guardo ambas en la matriz vacia

        
    return matriz_posicion

def menu(matriz:list):
    
    matriz_cargada = None

    while True:
        
        opcion = (input("Bienvenido al programa de Registro de Notas!\n" \
        "[1] Cargar las notas de los alumnos\n" \
        "[2] Porcentaje de examenes aprobados por alumno\n" \
        "[3] Mostrar el alumno con mejor promedio\n" \
        "[4] Buscador de nota\n" \
        "[5] Salir\n" \
        "Ingrese la opcion deseada: "))
        

        if es_digito(opcion):
            match opcion:
                case '1':
                    matriz_cargada = cargar_matriz_notas(matriz)
                case '2':
                    if matriz_cargada is None:
                        print("Error: Matriz vacia. Debe cargar la matriz en la Opcion 1")
                        
                    else:
                        porcentaje_aprobados(matriz)
                case '3':
                    if matriz_cargada is None:
                        print("Error: Matriz vacia. Debe cargar la matriz en la Opcion 1")
                        
                    else:
                        promedio = mejor_promedio(matriz)
                        print(promedio)                                          
                case '4':
                    if matriz_cargada is None:
                        print("Error: Matriz vacia. Debe cargar la matriz en la Opcion 1")
                        
                    else:
                        nota = (input('Ingrese la nota que desea buscar: '))
                        posiciones_encontradas = buscar_nota(matriz,nota)
                        print(posiciones_encontradas)


                case '5':
                    print("Adios! :)")
                    break

                case _:
                    print("Error: La opcion ingresada no es valida")
   


                
                
