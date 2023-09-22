def maiores(lista,n) :
    
    lista.append(n)
    lista.sort()
    posicao= lista.index(n)
    
    return lista[posicao +1::]