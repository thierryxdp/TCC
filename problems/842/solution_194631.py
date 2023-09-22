def pontos_por_time (time):
    soma = 0
    for i in range(len(time)):
        for j in range(2):
            soma += time[i][2][j]
    return soma