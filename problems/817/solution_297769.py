#
#
#
#
def acima_da_media(lista):
    n=sum(lista)/len(lista)
    if not n in lista:
        list.append(lista,n)
        list.sort(lista)
        i=list.index(lista,n)
        lista=lista[-1:i:-1]
        list.reverse(lista)
        return lista
    else:
        i=list.index(lista,n)
        lista=lista[-1:i:-1]
        list.reverse(lista)
        return lista