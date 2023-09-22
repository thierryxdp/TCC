def maiores(lista,n):
    '''funcao que dado uma lista e um numero inteiro n retorna uma segunda lista com os valores maiores do que n da lista original
    list,int->list'''
    x=lista
    x.append(n)
    list.sort(x)
    y=x.index(n)
    w=len(x)
    return lista[:w]