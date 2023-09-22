def filtra_pares(tupla):
    ''' funç˜ao que recebe uma tupla com quatro elementos inteiros como
    parâmetro, e retorne uma nova tupla contendo apenas os elementos pares da tupla original,
    na mesma ordem em que se encontravam.
    tupla->tupla'''
    x=tupla[0]
    y=tupla[1]
    z=tupla[2]
    w=tupla[3]
    tupla=(x,y,z,w)
    if tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return (x,y,z,w)
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0:
        return (x,y,z)
    elif tupla[0]%2==0 and tupla[1]%2==0:
        return (x,y)
    elif tupla[0]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return (x,z,w)
    elif tupla[0]%2==0 and tupla[2]%2==0:
        return(x,z)
    elif tupla[2]%2==0 and tupla[3]%2==0:
        return (z,w)
    elif tupla[1]%2==0 and tupla[2]%2==0:
        return (y,z)
    elif tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return (y,z,w)
    elif tupla[0]%2==0:
        return (x,)
    elif tupla[1]%2==0:
        return (y,)
    elif tupla[2]%2==0:
        return (z,)
    elif tupla[3]%2==0:
        return (w,)
    else:
        return ()