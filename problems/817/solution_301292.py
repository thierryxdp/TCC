def insere(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero


def maiores(lista,n):
    lista_nova = insere(lista,n)
    indice = list.index(lista_nova,n)
    del lista_nova[:indice+1]
    if n in lista_nova:
        list.remove(lista_nova,n)
    return lista_nova

def acima_da_media(lista):
    media = sum(lista)/len(lista)
    return maiores(lista,media)