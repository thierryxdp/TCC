def faltante(l):
    '''Calcula e retorna o número que está faltando na lista de números inteiros dada.
    list-->int'''
    i=0
    p=1
    while i<len(l) and p in l:
        p=p+1
        i=i+1
    return p