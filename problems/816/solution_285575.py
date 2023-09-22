def maiores(lista_int,n):
    lista0=[n]
    
    lista=lista_int+lista0
    list.sort(lista)
    
    x=list.index(lista,n)
    
    return lista[x:]