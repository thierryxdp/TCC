def pontos_por_time(jogo):
    # Vitória 3 pontos
    # Empate 1 ponto
    # Derrota 0
    # Total de pontos somo de pontos dos dois jogos

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

    #jogo ida
    if p1[0] > p1[1]:
        resultado[time1] += 3
    elif p1[0] == p1[1]:
        resultado[time1] += 1
        resultado[time2] += 1
    else:
        resultado[time2] += 3


    #jogo volta
    if p2[0] < p2[1]:
        resultado[time1] += 3
    elif p2[0] == p2[1]:
        resultado[time1] += 1
        resultado[time2] += 1
    else:
        resultado[time2] += 3

    return resultado