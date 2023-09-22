def filtra_pares(tupla1):
    """ Função que recebe uma tupla com quatro elementos inteiros 
    como parâmetro, e retorna uma nova tupla contendo apenas os ele-
    mentos pares da tupla original, na mesma ordem em que se encontra-
    vam.
    Entrada: Tupla ( int,int,int,int )
    Saída: Tupla (int)
    """
    tupla1=a,b,c,d
    x=int(tupla1[0])%2
    y=int(tupla1[1])%2
    z=int(tupla1[2])%2
    w=int(tupla1[3])%2
    
    if x==0 and y==0 and z==0 and w==0:
        return a,b,c,d
    elif x==0 and y==0 and z==0 and not (w==0):
        return a,b,c
    elif x==0 and y==0 and w==0 and not(z==0):
        return a,b,d
    elif x==0 and z==0 and w==0 and not (y==0):
        return a,c,d
    elif y==0 and z==0 and w==0 and not(x==0):
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
    elif x==0 and not(y==0) and not (z==0) and not (w==0):
        return a
    elif y==0 and not(x==0) and not(z==0) and not(w==0):
        return b
    elif z==0 and not(x==0) and not (y==0) and not(w==0):
        return c
    elif w==0 and not(x==0) and not(y==0) and not(z==0):
        return d
    else:
        return None