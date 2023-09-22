def busca(setor,matriz):
    '''Dada uma matriz de dados de funcionarios e um setor, retorna todos os funcionários da matriz que são daquele setor.
    matriz, str -> matriz'''
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor in matriz[i]:
                lista = matriz[i]
                matriz[i].remove(setor)
                return [lista]
           
    
    return []