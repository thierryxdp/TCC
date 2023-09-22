def maiores(lista,n):
    
    lista= lista.append(n)
    lista=list.sort(lista)
    novalista= lista.index(n)
    
    novalista= novalista[n:]
    
    return novalista