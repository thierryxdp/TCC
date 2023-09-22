def conta_numero(numero,matriz):
    """essa funcao calcula que dado um numero inteiro e uma matriz qualquer, conta e retorna quantas vezes aquele numero aparece na matriz; int, list-> int""" 
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                contador+=1
    return contador