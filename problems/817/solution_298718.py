def acima_da_media(lista, c=0):
    list.sort(lista)
    c = sum(lista)/2
    if lista[0] < c:
        return lista[len(lista)//2:]
    
    elif lista[len(lista)-1] < c:
        return [lista[len(lista)-1]]