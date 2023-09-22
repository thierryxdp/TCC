def busca(setor,matriz):
    '''recebe uma matriz com informacoes de funcionarios e retorna uma lista
    com as informacoes dos funcionarios dado o setor na entrada
    str,list->list'''
    listaReturn = []
    for i in matriz:
        if i[2]==setor:
            listaReturn += [i[0],i[1],i[3]]
    return listaReturn