def busca(setor,matriz):
    '''faz uma busca por setor, dado um setor da empresa, retorna os dados de todos os funcionarios desse setor.string,lista->lista'''
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(lista,[matriz[i]])
            del lista[i][2]
    return lista