def busca(setor,matriz):
    '''Dada uma matriz com as informações de cada
    funcionário e o setor desejado, retorna todas
    as informações sobre os funcionários daquele
    setor.
    str, list -> list'''
    r = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == setor:
                r += [matriz[i].remove(j)]     
    return r