def maiores(lista,n):
    
    lista= lista.append(n)
    lista=lista.sorted()
    novalista= lista.index(n)
    
    novalista= novalista[n:]
    
    return novalista