def maiores(lista,n):
    if n not in lista:
        list.append(lista,n)
    if n in lista:
        list.sort(lista)
        a=list.index(lista,n)
        lista2=lista[a+1:]
        return lista2      
def acima_da_media(lista2):
    media=sum(lista2)/len(lista2)
    return(maiores(lista2,media))