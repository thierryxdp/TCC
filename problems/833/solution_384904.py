def conta_numero(numero, matriz):
    """Função que dado um numero busca o mesmo na matriz dada
    int, int -> int"""
    contador=0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero in matriz[i][j]:
                contador+=1
    return contador