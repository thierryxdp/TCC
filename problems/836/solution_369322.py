def busca(setor, matriz):
    '''Funcao que retorna os dados dos
    funcionarios pertencentes a tal setor
    str, list -> list
    '''
    r = []
    y = 0
    linha = len(matriz)
    coluna = len(matriz[0])
    for x in range(linha):
        if matriz[x][2] == setor:
            y =+ 1
            r.insert(y, matriz[x])
            r[x].remove(matriz[y][2])
    return r