def acima_da_media(lista):    
    n = len(lista)  
    s = sum(lista)        
    m = s/n

    if m not in lista:
        lista.append(m)
        list.sort(lista)
        i = list.index(lista, m)+1
        l = lista[i:]
        return l
    else:
        list.sort(lista)
        i = list.index(lista, m)
        l = lista[i:]
        return l