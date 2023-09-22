def pontos_por_time(lista):
    """Função"""
    lista1 = lista[0]
    lista2 = lista[1]
    placar1 = lista1[2]
    placar2 = lista2[2]
    if str(lista1[0]) == str(lista2[0]):
        if placar1[0] > placar1[1] and placar2[0] > placar2[1]:
            return {lista1[0] : 6, lista1[1] : 0}
        elif placar1[0] > placar1[1] and placar2[0] < placar2[1]:
            return {lista1[0] : 3, lista1[1] : 3}
        elif placar1[0] < placar1[1] and placar2[0] < placar2[1]:
            return {lista1[0] : 0, lista1[1] : 6}
        elif placar1[0] == placar1[1] and placar2[0] == placar2[1]:
            return {lista1[0] : 2, lista1[1] : 2}
        elif placar1[0] > placar1[1] and placar2[0] == placar2[1]:
            return {lista1[0] : 4, lista1[1] : 1}
        elif placar1[0] == placar1[1] and placar2[0] > placar2[1]:
            return {lista1[0] : 4, lista1[1] : 1}
        elif placar1[0] == placar1[1] and placar2[0] < placar2[1]:
            return {lista1[0] : 1, lista1[1] : 4}
        elif placar1[0] < placar1[1] and placar2[0] > placar2[1]:
            return {lista1[0] : 3, lista1[1] : 3}
    elif str(lista1[0]) != str(lista2[0]):
        if placar1[0] > placar1[1] and placar2[0] > placar2[1]:
            return {lista1[0] : 3, lista1[1] : 3}
        elif placar1[0] > placar1[1] and placar2[0] < placar2[1]:
            return {lista1[0] : 6, lista1[1] : 0}
        elif placar1[0] < placar1[1] and placar2[0] < placar2[1]:
            return {lista1[0] : 3, lista1[1] : 3}
        elif placar1[0] == placar1[1] and placar2[0] == placar2[1]:
            return {lista1[0] : 2, lista1[1] : 2}
        elif placar1[0] > placar1[1] and placar2[0] == placar2[1]:
            return {lista1[0] : 4, lista1[1] : 1}
        elif placar1[0] == placar1[1] and placar2[0] > placar2[1]:
            return {lista1[0] : 1, lista1[1] : 4}
        elif placar1[0] == placar1[1] and placar2[0] < placar2[1]:
            return {lista1[0] : 4, lista1[1] : 1}
        elif placar1[0] < placar1[1] and placar2[0] > placar2[1]:
            return {lista1[0] : 6, lista1[1] : 0}