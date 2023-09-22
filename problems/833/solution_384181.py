def conta_numero(numero,matriz):
    """
    Função que recebe um numero e uma matriz e conta quantas vezes esse
    numero aparece na matriz
    int,list -> int
    
    Parâmetros:
    Entrada: numero, matriz
    Retorna: quantidade de vezes que o número repete
    """
    
    contador = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero == matriz[i][j]:
                contador+=1
    return contador