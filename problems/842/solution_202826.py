def pontos_por_time(jogo1, jogo2):
    timeA = jogo1[0][0]
    timeB = jogo1[0][1:2]
    a1 = jogo1[0][2:3][0]
    b1 = jogo1[0][2:3][0]
    b2 = jogo2[1:2][2:3][0:]
    a2 = jogo2[1:2][2:3][1:2]

    pontosA = []
    pontosB = []

    if a1>b1:
        pontosA = pontosA + 3
    elif a1 == b1:
        pontosA = pontosA + 1
        pontosB = pontosB + 1
    else:
        pontosB = pontosB + 3

    if a2>b2:
        pontosA = pontosA + 3
    elif a2 == b2:
        pontosA = pontosA + 3
        pontosB = pontosB + 3
    else:
        pontosB = pontosB + 3
    
    times = {"timeA": pontosA, "timeB": pontosB}
    return times