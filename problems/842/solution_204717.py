def pontos_por_time(jogo):
    """  [[’Cormengo’,’Flaminthians’, [1, 0]],
    [’Flamınthians’, ’Cormengo’, [2, 2]]]
    """
    jogo1 = jogo[0] 
    jogo2 = jogo[1]
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