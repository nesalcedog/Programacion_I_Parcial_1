# 1 – Función cargar_matriz_notas(): Recibe dos enteros n y m y permite
# cargar n x m notas válidas entre 1 y 10 inclusive. La validación debe
# hacerse dentro de esta función.
# 2 – Función porcentaje_aprobados(): Calcula el porcentaje de
# exámenes aprobados (nota ≥ 6) por cada alumno y muestra un resumen
# individual. Usar contadores y acumuladores.



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
    print(matriz)
    


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


##Prueba de las funciones
# alumnos_x_examenes = []
# cargar_matriz_notas(alumnos_x_examenes)
# porcentaje_aprobados(alumnos_x_examenes)

