def filtra_pares(a,b,c,d):
    """ Função que recebe uma tupla contendo quatro elementos inteiros
    como parâmetro e retorna uma tupla contendo apenas os elementos pares
    na mesma ordem em que se encontravam.
    Entrada: Tupla
    Saída: Tupla
    """
    x=a%2
    y=b%2
    z=c%2
    w=d%2
    
    
    if x==0 and y==0 and z==0 and w==0:
        return a,b,c,d
    elif x==0 and y==0 and z==o and not (w==0):
        return a,b,c
    elif x==0 and y==0 and w==0 and not(z==0):
        return a,b,d
    elif x==0 and z==0 and w==o and not (y==0):
        return a,c,d
    elif y==0 and z==0 and w==o and not(x==0):
        return b,c,d
    elif x==0 and y==0 and not(z==0) and not(w==0):
        return a,b
    elif x==0 and z==0 and not(y==0) and not (w==0):
        return a,c
    elif x==0 and w==0 and not(y==0) and not(z==0):
        return a,d
    elif y==0 and z==0 and not(x==0) and not(w==0):
        return b,c
    elif y==0 and w==0 and not(x==0) and not(z==0):
        return b,d
    elif z==0 and w==0 and not(x==0) and not(y==0):
        return c,d
    else:
        return None