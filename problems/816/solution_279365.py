def maiores(lista,n):
    '''retorna todos os numeros da lista maiores
    que n; list, int -> int'''
    list.sort(lista)
    n=list.index(lista)
    return lista[n:]