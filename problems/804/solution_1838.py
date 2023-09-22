#Start your python function here
def filtra_pares(t):
    """Recebe uma tupla com quatro elementos inteiros e retorna uma tupla
       contendo apenas os elementos pares da tupla original;
       tuple->tuple
    """
       
    x,y,z,w=t
    if x%2==0 and y%2==0 and z%2==0 and w%2==0:
        return x,y,z,w
    elif x%2==0 and y%2==0 and z%2==0:
        return x,y,z
    elif x%2==0 and y%2==0:
        return x,y
    elif x%2==0 and z%2==0 and w%2==0:
        return x,z,w
    elif x%2==0 and z%2==0:
        return x,z
    elif x%2==0 and w%2==0:
        return x,w
    elif x%2==0:
        return x,
    elif y%2==0 and z%2==0 and w%2==0:
        return y,z,w
    elif y%2==0 and z%2==0:
        return y,z
    elif y%2==0 and w%2==0:
        return y,w
    elif y%2==0:
        return y,
    elif z%2==0 and w%2==0:
        return (z,w)
    elif z%2==0:
        return z,
    elif w%2==0:
        return w,
    else:
        return ()