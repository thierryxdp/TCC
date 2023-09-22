def maiores(lista,n):
    
    lista= lista.append(n)
    lista=lista.sort()
    novalista= lista.index(n)
    
    novalista= novalista[n:]
    
    return novalista