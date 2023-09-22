def conta_numero(numero, matriz):
    '''Função que conta quantas vezes aquele número aparece na matriz, list -> int'''
    quantidade = 0
    for i in matriz:
        for j in i:
            if j == matriz:
                quantidade = quantidade + 1
    return quantidade