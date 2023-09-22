def maiores(lista,n):
    '''maiores recebe uma lista de números e um inteiro n e retoma uma nova lista que contém todos os números da lista original maiores que n.
    list,int-->list'''
    list.append(lista,n)
    list.sort(lista)
    x=list.index(lista,n)+1
    return lista[x:]