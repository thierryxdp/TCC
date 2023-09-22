def acima_da_media(lista):
    """ """
    lista_saida = []
    tam = len(lista)
    for i in lista:
        i += lista[i]
    media = i / tam
    for i in lista:
       if i > media:
            lista_saida.append(i)
    lista_saida.sort()
    return lista_saida