def busca(setor,matriz):
    '''esta função retorna todos os funcionarios de um setor. str,list(list)->list(list)'''
    f = []
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            if setor == matriz[x][y]:
                f.append(matriz[x])
    for x in range(len(f)):
        for y in range(len(f[0])):
            if setor in f[x]:
                f[x].remove(setor)
    return f