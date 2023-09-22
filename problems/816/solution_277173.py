def maiores(a,b):
    '''Dada uma lista de números inteiros(a) e
    um número inteiro(b), retorna outra lista que
    contém todos os números da lista original maiores
    que (b).
    list --> list'''
    x=a[:]
    list.append(x,b)
    list.sort(x)
    y = list.index(x,b)
    return x[y:]