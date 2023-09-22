def pontos_por_time(rodadas):
    pontostime1 = 0
    pontostime2 = 0
    if rodadas[0][2][0] > rodadas[1][2][0] or rodadas[0][2][1] > rodadas[1][2][1]:
        pontostime1 = pontostime1 + 3
    elif rodadas[0][2][0] < rodadas[1][2][0] or rodadas[0][2][1] < rodadas[1][2][1]:
        pontostime2 = pontostime2 + 3
    else:
        pontostime1 = pontostime1 + 1
        pontostime2 = pontostime2 + 1
    return {rodadas[0][0] : pontostime1 , rodadas[1][0] : pontostime2}