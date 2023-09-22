def pontos_por_time (lista):
    time_a = lista [0][0]
    time_b = lista [0][1]
    golstime_a1 = lista [0][2][0]
    golstime_b1 = lista [0][2][1]
    time_a == lista [1][1]
    time_b == lista [1][0]
    golstime_a2 = lista [1][2][1]
    golstime_b2 = lista [1][2][0]
    pontos_time_a = 0
    pontos_time_b = 0
    if golstime_a1 > golstime_b1:
        pontos_time_a = +3
    if golstime_a1 == golstime_b1:
        pontostime_a = +1
        pontostime_b = +1
    if golstime_a1 < golstime_b1:
        pontostime_b = +3
    if golstime_a2 > golstime_b2:
        pontostime_a = +3
    if golstime_a2 == golstime_b2:
        pontostime_a = +1
        pontostime_b = +1
    if golstime_a2 < golstime_b2:
        pontostime_b = +3
    return {time_a: pontostime_a, time_b: pontostime_b}