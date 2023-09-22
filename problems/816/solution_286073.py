def maiores(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero)
    x=list.index(lista_numero,n)
    if  list.count(lista_numero,n)==1:
        lista_numero2=lista_numero[:x]
    else:
        lista_numero2=lista_numero[:x+list.count(lista_numero,n)]
    
    return lista_numero2