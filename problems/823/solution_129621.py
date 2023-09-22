def faltante(lista):
    '''Dada uma lista de n-1 números inteiros numerados de 1 a n, descobre qual número está faltando'''
    '''list->int'''
    list.sort(lista)
    completa=[]
    x=1
    while len(completa)<=len(lista):
        completa=completa+[x]
        x=x+1
    return sum(completa)-sum(lista)