def maiores(lista,n):
    if n not in lista:
            list.insert(lista,0,n)
    list.sort(lista)
    local_De_n = list.index(lista,n)
    lista = lista(local_De_n+1:)
    return lista

def acima_da_media(notas):
    media = sum(notas)/len(notas)
    return maiores(notas, media)