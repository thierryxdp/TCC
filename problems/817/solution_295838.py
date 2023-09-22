def maiores(lista,n):
    listax=[]
    list.append(lista,n)
    list.sort(lista)
    a=list.index(lista,n)
    lista2=lista[a+1:]
    if len(lista)==0:
        return listax
    return lista2


def acima_da_media(lista2):
    media=sum(lista2)/len(lista2)
    return(maiores(lista2,media))