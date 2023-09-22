def total(lista,v):
    produtos= dict.keys(v)
    valores= dict.values(v)
    r=0

    for x in lista:
        r=r+dict.get(x)
    return r