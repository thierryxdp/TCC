def busca(setor,mat):
    '''função que recebe uma matriz(mat) e busca pelo setor de uma empresa
    informado, retorna os dados de todos os funcionários daquele setor.
    str,list->list'''
    matriz=[]
    for i in mat:
        lista=[]
        for j in i:
            if j == setor:
                lista.append(i[0])
                lista.append(i[1])
                lista.append(i[3])
        if lista!=[]:
            matriz.append(lista)
    return matriz