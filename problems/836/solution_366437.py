def busca(setor,matriz):
    '''esta função retorna todos os funcionarios de um setor. str,list(list)->list(list)'''
    funcionarios = []
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            if setor == matriz[x][y]:
                funcionarios.append(x)
    funcionarios.remove(setor)
    return funcionarios