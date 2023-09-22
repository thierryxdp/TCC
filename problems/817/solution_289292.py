def maiores(lista1, n):
    list.append(lista1, n)
    list.sort(lista1)
    posicao_n=list.index(lista1, n)
    nova_lista = lista1[(posicao_n):]
    del(nova_lista[posicao_n])
    return nova_lista
def acima_da_media(lista):
        media = sum(lista)/len(lista)
        lista_maiores = maiores(lista,media)
        return lista_maiores