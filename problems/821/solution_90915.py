def fatorial (n):
    '''função que dado um número (n) retorna o seu fatorial;
    int->int'''
    lista=[]
    sub=1
    while sub>1:
        lista+=n*(n-sub)
    sub+=1
    return lista