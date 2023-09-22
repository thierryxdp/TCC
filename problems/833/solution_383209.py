def conta_numero(numero,matriz):
    """ essa função irá retornar quantas vezes o numero apareceu na matriz dada
entrada -> int,list
saida -> int """
    vezes = 0
    for a in range(len(matriz)):
        for b in range(len(matriz[a])):
            if numero == matriz[a][b]:
                vezes += 1
    return vezes