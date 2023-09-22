def faltante(lista):
    '''função que dada uma lista com n-1 inteiros numerados e 1 a n retorna o valor que está faltando:list-->int'''
    lista.append(0)
    lista.sort()
    i = 0
    resp = 0
    
    while i <= len(lista):
        if(i != lista [i-1] and i != 0):
            resp = i
        i += 1
    return resp