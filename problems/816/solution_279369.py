def maiores(lista,n):
    '''retorna todos os numeros da lista maiores
    que n; list, int -> int'''
    list.append(lista,n)
    list.sort(lista)
    posicao=list.index(lista,n)
    return lista[posicao+1:]