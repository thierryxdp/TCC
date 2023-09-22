def faltante(l):
    '''Função que descobre qual número inteiro está faltando em uma lista
    de números inteiros: list -> int'''
    n=len(l)
    i=0
    f=0
    l2=list(range(1,n+2))
    
    while i<len(l2):
        if l2[i] not in l:
            f = f + l2[i]
        i=i+1
    return f