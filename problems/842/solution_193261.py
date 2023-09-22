def pontos_por_time(lista):
    ida = lista[0]
    volta = lista[1]
    placar_ida = ida[2]
    placar_volta = volta[2]
    if placar_ida[0]+placar_volta[1] > placar_ida[1]+placar_volta[0]:
        return {ida[0]:6,ida[1]:0}