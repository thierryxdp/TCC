def conta_numero(numero, matriz):
    '''Função que conta quantas vezes aquele número aparece na matriz, list -> int'''
    quantidade = 0
    lista = []
    for i in matriz:
        for j in i:
            if j == numero:
                quantidade = quantidade + 1
    return quantidade