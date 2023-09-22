def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    x=lista
    return [lista for lista in lista if lista>n]
def acima_da_media(lista):
    a=sum(lista)
    b=len(lista)
    c=a/b
    return maiores(lista,c)