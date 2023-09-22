def maiores(lista, x):
    if x not in lista:
        list.insert(lista,0,x)
    list.sort(lista)
    
    fati = list.index(lista,x)
    lista2 = lista[fati+1:]
    
    return lista2
    
def acima_da_media(notas):
    x=sum(notas)/len(notas)
    return maiores(notas,x)