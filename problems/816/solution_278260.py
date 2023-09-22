def maiores(lista,n):
    
    lista.append(n)
    lista.sort()
    novalista= lista.index(n)
    
    novalista= novalista[n:]
    
    return novalista