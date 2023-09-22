def pontos_por_time(jogo):
    """que receba uma lista de dois elementos, onde cada um
desses elementos  ́e também uma lista. A lista completa tem informa ̧cões do numero de gols em dois
jogos de futebol entre dois times (jogo da ida e jogo da volta), no seguinte formato: [[’Cormengo’,
’Flaminthians’, [1, 0]], [’Flamınthians’, ’Cormengo’, [2, 2]]].
    """
    j1 = jogo[0]
    j2 = jogo[1]
    t1 = j1[0]
    t2 = j1[1]
    assert j2[0] == t2
    assert j2[1] == t1

    p1 = j1[2]
    p2 = j2[2]

    resultado = {}
    resultado[t1] = 0
    resultado[t2] = 0

    if p1[0] > p1[1]:
        resultado[t1] += 3
    elif p1[0] == p1[1]:
        resultado[t1] += 1
        resultado[t2] += 1
    elif p1[0] < p1[1]:
        resultado[t2] += 3

    if p2[0] < p2[1]:
        resultado[t1] += 3
    elif p2[0] == p2[1]:
        resultado[t1] += 1
        resultado[t2] += 1
    elif p2[0] > p2[1]:
        resultado[t2] += 3
        return resultado