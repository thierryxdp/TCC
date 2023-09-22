def faltante(l):
    '''Dada uma lista de inteiros partindo de 1, retorne o número N faltante.
assinatura: list --> int
exemplo:
faltante([1,2,5,3])==4'''
    c=1
    i=1
    while i<=len(l):
        if i not in l:
            c=i
        else:
            if i==max(l):
                c=i+1
        i=i+1
    return c