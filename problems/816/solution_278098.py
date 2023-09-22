def maiores(lista,n):
    
    lista.append(n)
    lista.sort()
    
    posicao = lista.index(n)+1
    lista=lista[posicao]
    
    return lista