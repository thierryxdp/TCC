def maiores(lista,n):
    '''Função que retorna os números maiores do que n, presentes na lista
    inicial; list, int -> list'''
    l=lista
    list.append(l,n)
    list.sort(l)
    i=list.index(l,n)
    del l[:i]
    return l