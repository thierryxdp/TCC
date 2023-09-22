def busca(setor,m):
    '''Dado o setor e a matriz de funcionarios, a funcao retorna uma matriz
    com os funcionarios daquele setor.
    str, list -> list'''
    funcionarios=[]
    for i in range(len(m)):
        if m[i][2]==setor:
            funcionario=m[i].remove(setor)
            funcionarios.append(funcionario)
    return funcionarios