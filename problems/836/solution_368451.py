def busca(setor,matriz):
    '''Dada uma matriz de dados de funcionarios e um setor, retorna todos os funcionários da matriz que são daquele setor.
    matriz, str -> matriz'''
    lista = []
    lista1=[]
    for i in matriz:
        for j in i:
            if setor in matriz[i]:
                lista = matriz[i]
                matriz[i].remove(setor)
                list.append(lista1,lista)
                return lista1
           
    
    return []