def maiores(lista,n):
    lista=sorted(lista)
    if n in lista:
        return sorted(lista)    
    else:
        return lista[n:]