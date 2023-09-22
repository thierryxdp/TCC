def acima_da_media(lista):
    """ """
   	saida = list
    tam = len(lista)
    for i in lista:
        i += lista[i]
    media = i / tam
    for i in lista
       if i > media:
            saida.append(i)
    saida.sort()
    return saida