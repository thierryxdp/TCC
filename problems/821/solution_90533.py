def fatorial(n): 
    '''funçao retorna o calculo fatorial do numero de entrada''' 
    '''int->int'''
    i=n-1
    resultado=n
    while i > 0:
        if n*i:
            resultado=resultado*i
        i=i-1 
    return resultado