def maiores(lista_int,n):
    '''FunÃ§Ã£o que recebe uma lista de nÃºmeros inteiros, um nÃºmero inteiro n
        e retorna uma outra lista com todos os nÃºmeros da lista original que
        sÃ£o maiores que n.'''
    list.insert(lista_int,0,n)
    list.sort(lista_int,reverse=True)
    x = list.index(lista_int,n,0)
    del lista_int[x::]

    return lista_int[::-1]