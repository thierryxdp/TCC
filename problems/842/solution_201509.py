def pontos_por_time(rodadas):
    pontostime1 = 0
    pontostime2 = 0
    if rodadas[1][3][1] > rodadas[2][3][1] or rodadas[1][3][2] > rodadas[2][3][2]:
        pontostime1 = pontostime1 + 3
    elif rodadas[1][3][1] < rodadas[2][3][1] or rodadas[1][3][2] < rodadas[2][3][2]:
        pontostime2 = pontostime2 + 3
    else:
        pontostime1 = pontostime1 + 1
        pontostime2 = pontostime2 + 1
    return {rodadas[1][1] : pontostime1 , rodadas[2][1] : pontostime2}