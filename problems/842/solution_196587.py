def pontos_por_time(lista):
    """Função que recebe uma lista de dois elementos onde cada elemento é também uma lista.
    A lista completa tem informações do número de gols em dois jogo de futebol.
    Essa função retorna um dicionário cujos mapeamentos são o <nome do time> -> <número total de pontos na fase>.
    Os pontos de um time são calculados da seguinte forma: em cada jogo, os times recebem três pontos por vitória
    e um ponto por empate. Não são atribuídos pontos para derrotas. O total de pontos de uma fase é a soma de pontos dos dois jogos da fase."""
    lista[0] = lista1
    lista[1] = lista2
    lista1[2] = placar1
    lista2[2] = placar2
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