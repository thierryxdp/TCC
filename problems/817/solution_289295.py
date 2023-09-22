def maiores(lista1, n):
    list.append(lista1, n)
    list.sort(lista1)
    posicao_n=list.index(lista1, n)
    return lista1[(posicao_n+1):]
def acima_da_media(lista):
    media = sum(lista)/len(lista)
    list.sort(lista)
    lista_maiores = maiores(lista, media)
    return lista_maiores