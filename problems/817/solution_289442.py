def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    x=list.index(lista,n)
    return lista[x+1:]
def acima_da_media(notas):
    media=(sum(notas)/len(notas))
    return maiores(notas,media)