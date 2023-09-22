def maiores(lista,n):
    ''' Função que,dada uma lista de numeros inteiros e um numero n,retorna outra lista
    que contém todos os numeros da lista original maiores que n.
    list,int-->list'''
    if n not in lista:
        list.append(lista,n)
        list.sort(lista)
        posicao = list.index(lista,n)
        del lista[0:posicao+1]
        return lista
    if n in lista:
        list.sort(lista)
        quantasvezes = list.count(lista,n)
        posicao = list.index(lista,n)
        del lista[0:(posicao+quantasvezes)]
        return lista