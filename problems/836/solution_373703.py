def busca(setor,matriz):
    '''Dado uma matriz, com as informações dos
    funcionários e o setor desejado, retorna as
    informações sobre todos os funcionários daquele
    setor.
    str, list -> list'''
    r = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == setor:
                s = list.del(matriz[i],2)
                r += s
    return r