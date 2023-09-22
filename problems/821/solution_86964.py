def fatorial(n):
    '''Função que calcula o fatorial do número n dado como entrada. int->int'''
    mult=1
    c=1
    lista_f= list(range(n+1))
    while c<len(lista_f):
        mult= mult*lista_f[c]
        c=c+1
    return mult