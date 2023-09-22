def pontos_por_time(lista):
    """Função que retorna um dicionário cujos mapeamentos são: <nome do time> -> <número total de pontos na fase>,
    quando inserido como entrada uma lista de dois elementos, onde cada elemento é também uma lista, no primeiro elemento,
    a lista deve conter o nome dos dois times e no segundo elemento a lista deve conter o placar em dois jogos entre
    esses dois times. Os pontos de um time na fase são calculados da seguinte forma: em cada jogo, os times recebem
    três pontos por vitória e um ponto por empate. Não são atribuídos pontos para derrotas."""
    lista1 = lista[0]
    lista2 = lista[1]
    placar1 = lista1[2]
    placar2 = lista2[2]
    if str(lista1[0]) == str(lista2[0]):
        if placar1[0] > placar1[1] and placar2[0] > placar2[1]:
            return {lista1[0] : 6, lista1[1] : 0}
        elif placar1[0] > placar1[1] and placar2[0] < placar2[1]:
            return {lista1[0] : 3, lista1[1] : 3}#Start your python function here