def pontos_por_time(jogo):
    """que receba uma lista de dois elementos, onde cada um
desses elementos  ́e também uma lista. A lista completa tem informa ̧cões do numero de gols em dois
jogos de futebol entre dois times (jogo da ida e jogo da volta), no seguinte formato: [[’Cormengo’,
’Flaminthians’, [1, 0]], [’Flam ́ınthians’, ’Cormengo’, [2, 2]]].
    """
    jogo1 = jogo[0]
    jogo2 = jogo[1]
    time1 = jogo1[0]
    time2 = jogo1[1]
    assert jogo2[0] == time2
    assert jogo2[1] == time1

    p1 = jogo1[2]
    p2 = jogo2[2]

    resultado = {}
    resultado[time1] = 0
    resultado[time2] = 0

    if p1[0] > p1[1]:
        resultado[time1] += 3
    elif p1[0] == p1[1]:
        resultado[time1] += 1
        resultado[time2] += 1
    else:
        resultado[time2] += 3

    if p2[0] < p2[1]:
        resultado[time1] += 3
    elif p2[0] == p2[1]:
        resultado[time1] += 1
        resultado[time2] += 1
    else:
        resultado[time2] += 3
        return resultado