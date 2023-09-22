#
#
#
#
def acima_da_media(lista):
    n=sum(lista)/len(lista)
    round(n,0)
    list.append(lista,n)
    list.sort(lista)
    i=list.index(lista,n)
    lista=lista[-1:i:-1]
    list.reverse(lista)
    return lista