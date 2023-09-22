def acima_da_media(lista):
    '''função que recebe uma lista e devolve outra lista com
    os valores que ficaram acima da média dos valores da lista
    dada'''
    lista_maior = []
    media = sum(lista)/(len(lista))
    for i in lista:
        if i > media:
            lista_maior.append(i)
            lista_maior.sort()
    return lista_maior