def filtraMultiplos(l,n):
    '''Dada uma lista e um número retorna uma nova lista com os multiplos de n contidos na primeira lista l.
assinatura: list --> list'''
    r=[]
    for x in l:
        if x%n==0:
            r.append(x) # = list.append(r,x)
    return r