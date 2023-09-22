def maiores(lista,n):
    
    lista.append(n)
    lista.sort()
    posição= lista.index(n)
    
   
    return lista[posição +1::]