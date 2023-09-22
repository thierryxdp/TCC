def filtra_pares(x):
    '''função que retorna só os elementos pares de determinada tupla
    de 4 parâmetros
    tupla-> tupla'''
    
    a= x[0]
    b= x[1]
    c= x[2]
    d= x[3]
    
    y= ()
    
    if a%2==0:
        return y + (a,)
    elif b%2==0:
        return y + (b,)
    elif c%2==0:
        return  y + (c,)
    elif d%2==0:
        return y + (d,)