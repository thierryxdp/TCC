def maiores(lista,n):
    list.sort(lista)
    for c in lista:
       
        if c>n:
            return lista[list.index(lista,c):]
            
        if c<n and n>c:
                return [lista[list.index(lista,c):]