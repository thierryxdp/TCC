def conta_numero(numero:int,matriz:list) -> int:
    acumuludador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
            	acumulador+=1
    return acumulador