def total(lista,v):
    produtos= dict.keys(v)
    valores= dict.values(v)
    r=0

    for x in lista:
        i=str.find(x,produtos)
        r=r+(valores[i])
    return r