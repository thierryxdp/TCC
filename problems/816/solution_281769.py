def maiores(lista,n):
    if n in lista:
        lista=list.sort(lista)
        list.count(lista,n)
        list.index(lista,n)
        
        return lista[list.count(lista,n)+list.index(lista,n):-1]