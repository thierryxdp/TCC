def filtra_pares(x):
    tupla_nova = tuple()
    if (x[0]%2) == 0:
        tupla_nova = tupla_nova +(x[0],)
    if (x[1]%2) == 0:
        tupla_nova = tupla_nova +(x[1],)
    if (x[2]%2) == 0:
        tupla_nova = tupla_nova +(x[2],)
    if (x[3]%2) == 0:
        tupla_nova = tupla_nova +(x[3],)
    return tupla_nova