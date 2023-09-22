def busca(setor, matriz):
    ''' Faz uma busca de funcionários pertecentes a um determinado setor 
    de uma empresa
    string, lista -> lista'''
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor.upper() in matriz[i][2].upper() and j==2:
                matriz[i].remove(matriz[i][2])
                lista+= matriz
    return lista