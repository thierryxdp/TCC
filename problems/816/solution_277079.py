def maiores(lista,n):
    if n in lista:
        posicao=list.index(lista,n)
        return lista[posicao+1:]
    
    if n not in lista:
        lista.append(n)
        list.sort(lista)
        posicao=list.index(lista,n)
        return lista[posicao+1:]