def busca(setor,matriz):
    '''A função recebe de entrada uma matriz e um determinado setor, e faz uma busca retornando todos os dados dos funcionários 
    daquele setor na empresa.str,list->list'''
    lista = []
    for s in range(len(matriz)):
        if setor in matriz[s]:
            list.remove(matriz[s],setor)
            lista = lista + [matriz[s]]
    return lista