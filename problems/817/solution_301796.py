def maiores(L,n):
    list.append(L,n)
    list.sort(L)
    indice = list. index(L,n)
    return L[indice+1:]

def acima_da_media(lista):
    '''Função que retorna uma lista ordenada com as notas que ficaram acima da média;
    list->list'''
    list.sort(lista)
    media = sum(lista)/len(lista)
    lista1 = maiores(lista,media)
    if int(media) in lista1:
        del lista1[0]
        return lista1
    if int(media) not in lista1:
        return lista1