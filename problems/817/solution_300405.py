def maiores(lista_numero,n):
    lista1 = lista_numero
    list.append(lista1,n)
    list.sort(lista1)
    lista_nova = lista1[list.index(lista1,n)+1:]
    return lista_nova

def acima_da_media(lista_nota):
    media = sum(lista_nota)/len(lista_nota)
    if media in nota:
        list.sort(lista_nota)
        lista = lista_nota[list.index(lista_nota,media)+1:]
        return lista