def maiores(lista,n):
    lista.append(n)
    lista.sort()
    lista=list[lista.index(n)+1]
    
    return lista