def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    x=list.index(lista,n)
    return lista[x+list.count(lista,n):]
def acima_da_media(notas):
    media=(sum(notas)/len(notas))
    return maiores(notas,media)