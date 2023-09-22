def maiores(lista,n):
    list.sort(lista)
    for c in lista and d in lista:
       
        if c>n:
            return lista
        
        if c<n and d>n:
            return lista[list.index(lista,c):]
            
        if c<n:
                return []