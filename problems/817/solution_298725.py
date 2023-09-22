def acima_da_media(lista, c=0):
    list.sort(lista)
    c = sum(lista)/2
    
    if len(lista) == 1:
        return []
    
    elif len(lista)//2 < c < lista(len(lista)-1):
        return lista[len(lista)-1]
    
    elif lista[0] < c:
        return lista[len(lista)//2:]