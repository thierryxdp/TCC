def busca(palavra,matriz):
    '''funcao que dado uma matriz e uma palavra, retorna todos os itens da linha em que a palavra se encontra
    list, str->list'''
    lista = []
    for x in matriz:
        if palavra == x[2]:
            list.append(lista,[x[0],x[1],x[3]])
    return lista