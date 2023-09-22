def conta_numero(n, matriz):
    """
    Função que dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes
    aquele número aparece na matriz.
    int,list -> int
    """
    contador = 0
    if matriz == []:
        return contador
    elif type(matriz[0]) == list:
        for i in range(len(matriz)):
            contador += matriz[i].count(n)        
    else:
        contador = matriz.count(n)
    return contador