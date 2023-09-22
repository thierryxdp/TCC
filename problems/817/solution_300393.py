def maiores(lista_int,n):
    list.append(lista_int,n)
    list.sort(lista_int)
    m = list.index(lista_int,n)
    maiores = lista_int[m+1:]
    return maiores
def acima_da_media(lista_notas):
    media = sum(lista_notas)/len(lista_notas)
    notas_acima_media = maiores(lista_notas,media)
    return notas_acima_media