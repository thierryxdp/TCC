def acima_da_media(lista):
    copia = list.copy(lista)
    soma = sum(copia)
    nelementos = len(lista)
    media = soma/nelementos
    for elem in list(lista):
    if elem < media:
    lista.remove(elem)
    return lista