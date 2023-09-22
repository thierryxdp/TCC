def grandes(inteiros,n):
    """funcao que recebe uma lista de notas e retorna uma nova lista com as notas que ficaram acima da media
    list -> list"""
    list.append(inteiros,n)
    list.sort(inteiros)
    ps=list.index(inteiros,n)
    lista=inteiros[ps+1:]
    return lista


def acima_da_media(lista):
    media=sum(lista)
    grandes=grandes(lista,media)
    return grandes