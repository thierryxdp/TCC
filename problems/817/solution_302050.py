def maiores(lista,n):
    """..."""
    listafinal=[]
    list.append(lista,n)
    for x in range(len(lista)):
        if lista[x] > n:
            listafinal.append(lista[x])  
    return sorted(listafinal)
    
    
    
def acima_da_media(notas):
    """..."""
    media=sum(notas)/(len(notas))
    return maiores(notas,media)