def maiores(lista,n):
    list.sort(lista)
    for c in lista:
       
        if c>n:
            return lista
        
        if c<n:
            return c