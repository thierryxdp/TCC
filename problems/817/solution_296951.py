def acima_da_media(lista):
    media = sum(lista) // len(lista)
    lista1 = []
    for nota in lista:
        if(nota > media):
        	lista1 = lista1 + [nota]
    lista1.sort()
    return lista1