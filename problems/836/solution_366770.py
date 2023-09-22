def busca(setor, x):
    """ Funçao que recebe uma matriz e faça uma busca por setor, retorna 
    os dados dos funcionarios.
    int-> str"""
    matriz=[]
    for i in range(len(x)):
        if setor in x[i][2]:
            del x[i][2]
            list.append(matriz, x[i])
    return matriz