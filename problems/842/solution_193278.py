def pontos_por_time(lista):
    ida = lista[0]
    volta = lista[1]
    placar_ida = ida[2]
    placar_volta = volta[2]
    if placar_ida[0] > placar_ida[1] and placar_volta[0] > placar_volta[1]:
        return {ida[0]:3, volta[0]:3}
    elif placar_ida[0] > placar_ida[1] and placar_volta[0] < placar_volta[1]:
        return {ida[0]:6, volta[0]:0}
    elif placar_ida[0] < placar_ida[1] and placar_volta[0] > placar_volta[1]:
        return {ida[0]:0, volta[0]:6}
    elif placar_ida[0] == placar_ida[1] and placar_volta[0] == placar_volta[1]:
        return {ida[0]:2, volta[0]:2}
    elif placar_ida[0] > placar_ida[1] and placar_volta[0] == placar_volta[1]:
        return {ida[0]:4, volta[0]:1}
    elif placar_ida[0] == placar_ida[1] and placar_volta[0] < placar_volta[1]:
        return {ida[0]:1, volta[0]:4}