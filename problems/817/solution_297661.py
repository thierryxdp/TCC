def maiores(lista_numero,n):
    lista=lista_numero+[n]
    list.sort(lista)
    x=list.index(lista,n)
    del lista[:x+1]
    return lista
def acima_da_media(notas):
    y= sum (notas)/len notas
    return maiores(notas,y)