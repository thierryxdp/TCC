def maiores(lista, n):
    if n not in lista:
        list.insert(lista,0,n)
    list.sort(lista)
    
    fati = list.index(lista,n)
    lista2 = lista[fati+1:]
    
    return lista2
    
def acima_da_media(notas):
    n=sum(notas)/len(notas)
    return maiores(notas,n)