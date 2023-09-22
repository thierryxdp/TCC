def pontos_por_time(jogo):
    """  [[’Cormengo’,’Flaminthians’, [1, 0]], primeiro jogo
    [’Flamınthians’, ’Cormengo’, [2, 2]]] segundo jogo
    """
    jogo1 = jogo[0] 
    jogo2 = jogo[1]
    time1 = jogo1[0]
    time2 = jogo1[1]
    jogo2[0] == time2
    jogo2[1] == time1
    
    pontos1 = jogo1[2]
    pontos2 = jogo2[2]

    resultado = {}
    resultado[time1] = 0
    resultado[time2] = 0

    if pontos1[0] > pontos1[1]:
        resultado[time1] += 3
    elif pontos1[0] == pontos1[1]:
        resultado[time1] += 1
        resultado[time2] += 1
    elif pontos1[0] < pontos1[1]:
        resultado[time2] += 3

    if pontos2[0] < pontos2[1]:
        resultado[time1] += 3
    elif pontos2[0] == pontos2[1]:
        resultado[time1] += 1
        resultado[time2] += 1
    elif pontos2[0] > pontos2[1]:
        resultado[time2] += 3
        return resultado