def filtra_pares(x):
    tupla = ()
    if x[1]%2==0:
        tupla = tupla+tuple(x[1])
    elif x[2]%2==0:
        tupla = tupla+tuple(x[2])
    elif x[3]%2==0:
        tupla = tupla+tuple(x[3])
    elif x[4]%2==0:
        tupla = tupla+tuple(x[4])
    return tupla