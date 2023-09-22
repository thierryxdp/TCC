def acima_da_media(lista):
    """ """
    lista_saida = []
    tam = len(lista)
    soma = int
    for i in lista:
        soma += lista[i]
    media = soma / tam
    for i in lista:
        if i > media:
            lista_saida.append(i)
    lista_saida.sort()
    return lista_saida