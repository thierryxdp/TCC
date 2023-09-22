def acima_da_media(lista):
    """Função que retorna uma lista com os as notas que ficaram acima da media; list->list """
    lista= sorted(lista)
    media= sum(lista)/(len(lista))
    resultado = []
    for i in range(len(lista)):
        if lista[i]>media:
            resultado.append(lista[i])

    return resultado