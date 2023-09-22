def filtraMultiplos(l,n):
    '''Dada uma lista e um número retorna uma nova lista com os multiplos de n contidos na primeira lista l.
assinatura: list --> list'''
    r=[]
    proximo=0
    while proximo<len(l):
        if l[proximo]%n==0:
            r = r+(l[proximo],)
        proximo=proximo+1
    return r