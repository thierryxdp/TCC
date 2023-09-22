def melhor_volta(m):
    minimo_geral = []
    volta = []
    for x in range(len(m)):
        for y in range(len(m[x])):
            if m[x][y] == min(m[x]):
                list.append(minimo_geral, m[x][y])
                list.append(volta, y)
    corredor = list.index(minimo_geral, min(minimo_geral)) + 1
    melhor_tempo = min(minimo_geral)
    melhor_volta = volta[corredor-1+1]
    return (corredor, melhor_tempo, melhor_volta)