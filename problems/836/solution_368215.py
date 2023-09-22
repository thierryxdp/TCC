def busca(setor,matriz):
    '''Dado uma matriz com dados de funcionários, retorna o resultado da busca pelo setor. list-> list.'''
    resultado =[]
    for i in range(0,len(matriz)):
        if matriz[i][2] == setor:
            list.append(resultado,matriz[i][:])
    for j in range(0,len(resultado)):
        del resultado[j][2]
    return resultado