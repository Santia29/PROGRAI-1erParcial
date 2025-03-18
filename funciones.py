#SANTIAGO ANLLO
def inicializar_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz:list) -> None:
    for fil in range(len(matriz)):
        #for col in range(len(matriz[0]))
        for col in range(len(matriz[fil])):
            print(matriz[fil][col],end=" ")
        print("")

def calcular_promedio_matriz(matriz):
    
    suma = 0
    contador = 0
    for fila in matriz:
        for num in fila[1:4]:
            suma += num
            contador += 1
    return suma // contador

# def calcular_porcentaje_de_votos(matriz):
#     suma_total = 0
#     for fila in matriz:
#         suma_total = fila[1] + fila[2] + fila[3]
#         for porcentaje in suma_total:
#             porcentaje = suma_total / 100

#     return porcentaje

#1 Carga de votos

def cargar_votos()-> list:
    votos_de_listas = inicializar_matriz(3,5,0)

    I_LISTA = 0
    VOTO_MAÑANA = 1
    VOTO_TARDE = 2
    VOTO_NOCHE = 3
    I_PORCENTAJE_VOTO = 4 
    
    mostrar_matriz(votos_de_listas)

    for fil in range(len(votos_de_listas)):
        print("\nINGRESO DE VOTOS:\n")
        
        numero_de_lista = int(str(input("Ingrese el numero de la lista(debe ser de tres cifras): ")))
        while numero_de_lista < 100:
            numero_de_lista = int(str(input("Reingrese el numero de la lista(debe ser de tres cifras): ")))

        votos_turno_mañana = int(input("TURNO MAÑANA: Ingrese la cantidad de votos: "))
        while votos_turno_mañana < 0:
            votos_turno_mañana = int(input("TURNO MAÑANA: Reingrese la cantidad de votos: "))
        
        votos_turno_tarde = int(input("TURNO TARDE: Ingrese la cantidad de votos: "))
        while votos_turno_tarde < 0:
            votos_turno_tarde = int(input("TURNO TARDE: Reingrese la cantidad de votos: "))
            
        votos_turno_noche = int(input("TURNO NOCHE: Ingrese la cantidad de votos: "))
        while votos_turno_noche < 0 :
            votos_turno_noche = int(input("TURNO NOCHE: Reingrese la cantidad de votos: "))

        
        votos_de_listas[fil][I_LISTA] = numero_de_lista
        votos_de_listas[fil][VOTO_MAÑANA] = votos_turno_mañana
        votos_de_listas[fil][VOTO_TARDE] = votos_turno_tarde
        votos_de_listas[fil][VOTO_NOCHE] = votos_turno_noche 
        nota_promiedo = calcular_promedio_matriz(votos_de_listas)##
        votos_de_listas[fil][I_PORCENTAJE_VOTO] = float(nota_promiedo)
        
    # for i in range(len(votos_de_listas)):
    #     print(f"Nro de lista:{votos_de_listas[i][I_LISTA]}\n CANTIDAD DE VOTOS TURNO MAÑANA: {votos_de_listas[i][VOTO_MAÑANA]}\n CANTIDAD VOTOS TURNO TARDE: {votos_de_listas[i][VOTO_TARDE]}\n CANTIDAD VOTOS TURNO NOCHE: {votos_de_listas[i][VOTO_NOCHE]}\n PORCENTAJE DE VOTOS: {votos_de_listas[i][I_PORCENTAJE_VOTO]}%\n")
    return votos_de_listas

cargar_votos_elecciones = cargar_votos()
#2
def mostrar_votos(votos_de_listas:list):
    
    I_LISTA = 0
    VOTO_MAÑANA = 1
    VOTO_TARDE = 2
    VOTO_NOCHE = 3
    I_PORCENTAJE_VOTO = 4 
    for i in range(len(votos_de_listas)):
        print(f"Nro de lista:{votos_de_listas[i][I_LISTA]}\n CANTIDAD DE VOTOS TURNO MAÑANA: {votos_de_listas[i][VOTO_MAÑANA]}\n CANTIDAD VOTOS TURNO TARDE: {votos_de_listas[i][VOTO_TARDE]}\n CANTIDAD VOTOS TURNO NOCHE: {votos_de_listas[i][VOTO_NOCHE]}\n PORCENTAJE DE VOTOS: {votos_de_listas[i][I_PORCENTAJE_VOTO]}%\n")
        
mostrar_votos(cargar_votos_elecciones)

def ordenar_de_forma_ascendente(matriz):
    I_TURNO_MAÑANA = 2
    I_LISTA = 0
    for i in range(len(matriz)-1):
        for j in range(i+1,len(matriz)):
            if (matriz[i][I_TURNO_MAÑANA] < matriz[j][I_TURNO_MAÑANA]):
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar
    print("\nORDEN DE MAYOR VOTOS TURNO MAÑANA:")
    for i in range(len(matriz)):
        print(f"LISTA: {matriz[i][I_LISTA]}")
        print(f"VOTOS TURNO MAÑANA: {matriz[i][I_TURNO_MAÑANA]}")

ordenar_de_forma_ascendente(cargar_votos_elecciones)


#4Encontrar y mostrar a las listas que tengan menos del 5% de todos los votos:

def mostrar_lista_con_menos_porcentaje_votos(matriz):
    I_LISTA = 0
    I_PORCENTAJE_VOTO = 4
    bandera = False
    for i in range(len(matriz)-1):
        for j in range(i+1,len(matriz)):
            if (matriz[i][I_PORCENTAJE_VOTO] > 5):
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar
                bandera == True
    print("\nLISTA/S QUE OBTUVIERON MENOS DEL 5%:")
    for i in range(len(matriz)):
        print(f"LISTA: {matriz[i][I_LISTA]}")
        print(f"PORCENTAJE DE VOTOS: {matriz[i][I_PORCENTAJE_VOTO]}")

    if bandera:
        print("No hay listas con menos del '5%' de los votos")

mostrar_listas_menos_votadas = mostrar_lista_con_menos_porcentaje_votos(cargar_votos_elecciones)

#5 

def mostrar_turno_con_mas_votos(matriz):
    I_VOTO_MAÑANA = 1
    I_VOTO_TARDE = 2 
    I_VOTO_NOCHE = 3 
    bandera = False
    for i in range(len(matriz)):
        
        if (matriz[i][I_VOTO_MAÑANA] > matriz[i][I_VOTO_TARDE]) and (matriz[i][I_VOTO_MAÑANA] > matriz[i][I_VOTO_NOCHE]):            
            print(f"El turno con mayor votos es TURNO MAÑANA: {matriz[i][I_VOTO_MAÑANA]}")
        
        elif (matriz[i][I_VOTO_TARDE] > matriz[i][I_VOTO_MAÑANA]) and (matriz[i][I_VOTO_TARDE] > matriz[i][I_VOTO_NOCHE]):            
            print(f"El turno con mayor votos es TURNO TARDE: {matriz[i][I_VOTO_TARDE]}")
        
        elif (matriz[i][I_VOTO_NOCHE] > matriz[i][I_VOTO_MAÑANA]) and (matriz[i][I_VOTO_NOCHE] > matriz[i][I_VOTO_NOCHE]):            
            print(f"El turno con mayor votos es TURNO NOCHE: {matriz[i][I_VOTO_NOCHE]}")
        
        bandera == True
    return bandera

mostrar_turno_con_mas_votos(cargar_votos_elecciones)
