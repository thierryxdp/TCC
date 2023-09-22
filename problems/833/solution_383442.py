def conta_numero(numero:int,matriz:list) -> int:
    """função que retorna o número de vezes que um dado número inteiro aparece em uma matriz.
    
    parâmetros:
    int, list -> list
    
    exemplos:
    conta_numero(1,[[1,1],[2,2]])==2
    conta_numero(3,[[3],[2]])==1
    conta_numero(4,[[1,1,5,6],[2,2,8,9]])==0
    """
    acumulador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
            	acumulador+=1
    return acumulador