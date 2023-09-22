def repetidos(n):
    ''' retorna o numero de vezes que um elemento é igual ao anterior na lista 
    tupla -> int'''
    r=0
    c=0
    p=0
    while c<len(n)-1:
        if n[p]==n[p+1]:
            r=r+1
        c=c+1
        p=p+1
    return r