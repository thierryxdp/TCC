def busca(setor,matriz):
    '''função que recebe um setor e uma mtriz e faz a busca
    e retorna os dados de todos os funcionários daquele setor.
    str,list->list'''
    matriz2=[]
    for i in matriz:
        lista=[]
        for j in i:
            if j ==setor:
                lista.append(i[0])
                lista.append(i[1])
                lista.append(i[3])
        if lista!=[]:
            matriz2.append(lista)
    return matriz2