def busca(setor, matriz):
    '''Funcao que retorna os dados dos
    funcionarios pertencentes a tal setor
    str, list -> list
    '''
    r = []
    linha = len(matriz)
    coluna = len(matriz[0])
    for x in range(linha):
        if matriz[x][2] == setor:
            r.insert(-1, matriz[x])
            r.remove(r[x][2])
    return r