def busca(setor, matriz):
    ''' função que procura dado uma matriz e
    um setor os funcionarios daquele setor
    list,str->list'''
    resultado = []
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if matriz[l][c] == setor:
                list.append(resultado,matriz[l][0:c]+matriz[l][c+1:])
    return resultado