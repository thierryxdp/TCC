def conta_numero(numero,matriz):
    """funcao que recebe um numero e uma matriz e retorna quantas vezes o numero aparece na matriz.
    entrada->int,list(list)
    saida-> int"""
    vezes=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero == matriz[i][j]:
                vezes+= + 1
    return vezes