#
#
#
#
def acima_da_media(lista):
    n=sum(lista)/len(lista)    
    list.append(lista,n)
    list.sort(lista)
    i=list.index(lista,n)
    lista=lista[i:]
    list.reverse(lista)
    return lista