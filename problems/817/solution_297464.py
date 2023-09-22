def maiores(lista,n):
    
    if n not in lista:
        
        list.insert(lista,0,n)
        list.sort(lista)
        k = list.index(lista,n)
        lista2 = lista[(k+1):]
        return lista2

    else:
        list.sort(lista)
        k = list.index(lista,n)
        lista3 = lista[(k+1):]
        return lista3
        

def acima_da_media(lista):
    
    media = sum(lista)/len(lista)
    
    return maiores(lista,media)