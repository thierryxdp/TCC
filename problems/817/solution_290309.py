def acima_da_media(lista):
    """retorna uma lista com as notas maiores que a media """
    lista_saida = []
    tam = len(lista)
    soma = 0
    for i in lista:
        soma += i
    media = soma / tam
    for i in lista:
        if i > media:
            lista_saida.append(i)
    lista_saida.sort()
    return lista_saida