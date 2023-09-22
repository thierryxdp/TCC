def maiores(lista, n):
    '''funcao que retorna uma nova lista com
    o inteiro n.
    entrada: lista, inteiro
    saida: lista
    '''
    list.insert(lista,0,n)
    list.sort(lista)
    posicao= list.index(lista,n)
    return lista[(posicao+1):]