def maiores(l,n):
    '''Dada uma lista de números inteiros e um inteiro n, retorna outra lista que contanha todos os números da lista original maiores que n.
assinatura: list --> list'''
    r=[]
    for e in l:
        if e>n:
            list.append(r,e)
    list.sort(r)
    return r