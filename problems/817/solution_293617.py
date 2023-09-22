def acima_da_media(lista):
    copia = list.copy(lista)
    soma = sum(copia)
    nelementos = len(lista)
    media = soma/nelementos
    lista = [x for x in lista if x !<= media]
    return media