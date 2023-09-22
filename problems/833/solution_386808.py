def conta_numero(numero,matriz):
    """Dadao um número inteiro e uma matriz, conta e retorna
    quantas vezes o número aparece na matriz
    int,list -> int"""
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero == matriz[i][j]:
                contador+=1
    return contador