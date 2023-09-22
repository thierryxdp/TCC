def faltante(lista):
    p = lista[0]
    u = lista[-1]
    listac = list(range(p, u + 1))
    
    nf = 0
    i = 0
    
    while contador < len(listac):
        if listac[i] not in lista:
            nf = listac[i] 
        i += 1
    return nf