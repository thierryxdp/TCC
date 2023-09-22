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
            r += matriz[x]
            r[x].remove(r[x][2])
    return r