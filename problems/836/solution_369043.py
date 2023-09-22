def busca(setor, matriz):
    ''' Faz uma busca de funcionários pertecentes a um determinado setor 
    de uma empresa
    string, lista -> lista'''
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor.upper() in matriz[i][j].upper():
                lista += matriz[i].pop(j)
   	return lista