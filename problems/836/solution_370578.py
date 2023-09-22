def busca(matriz,setor):
    ''' retorna uma lista como os funcionarios de cada setor
    lista,str -> lista
    '''
    funcionarios = []
    c = 0
    for i in matriz:
        if i[2] == setor:
            del(i[2])
            funcionarios.append(i)
            c += 1
    return funcionarios