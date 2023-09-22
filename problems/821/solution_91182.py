def fatorial(numero):
    
    '''calcula o fatorial de um número qualquer
    int --> int'''
    
    i = 1
    k=1
    lista = list()
    
    while i <= numero:
        k=k*i
        i=i+1
    return k