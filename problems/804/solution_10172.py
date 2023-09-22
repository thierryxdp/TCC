def filtra_pares(x,y,w,z):
    '''funcao que retorna quais sao os numeros pares da tupla
    de entrada
    (int,int,int,int) -> (int,int,int,int)'''
    if x%2==0 and y%2==0 and w%2==0 and z%2==0:
        return x,y,w,z
    elif x%2==0 and y%2==0 and w%2==0 and not z%2==0:
        return x,y,w
    elif x%2==0 and y%2==0 and not w%2==0 and z%2==0:
        return x,y,z
    elif x%2==0 and not y%2==0 and w%2==0 and z%2==0:
        return x,w,z
    elif not x%2==0 and y%2==0 and w%2==0 and z%2==0:
        return y,w,z
    elif x%2==0 and y%2==0 and not w%2==0 and not z%2==0:
        return x,y
    elif x%2==0 and not y%2==0 and w%2==0 and not z%2==0:
        return x,w
    elif x%2==0 and not y%2==0 and not w%2==0 and z%2==0:
        return x,z
    elif not x%2==0 and y%2==0 and w%2==0 and not z%2==0:
        return y,w
    elif not x%2==0 and y%2==0 and not w%2==0 and z%2==0:
        return y,z
    elif not x%2==0 and not y%2==0 and w%2==0 and z%2==0:
        return w,z
    elif x%2==0 and not y%2==0 and not w%2==0 and not z%2==0:
        return (x)
    elif not x%2==0 and y%2==0 and not w%2==0 and not z%2==0:
        return (y)
    elif not x%2==0 and not y%2==0 and w%2==0 and not z%2==0:
        return (w)
    elif not x%2==0 and not y%2==0 and not w%2==0 and z%2==0:
        return (z)
    else:
        return ()