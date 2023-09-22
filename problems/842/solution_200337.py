def pontos_por_time(lista):
    '''Função que recebe dois elementos sendo ambos uma lista contendo informções do placar
    de dois jogos, e retornar os pontos acumulados do time na fase
    list -> dict '''

    ida = lista[:1]
    volta = lista[1:2]
    time1 = lista[0][0]
    time2 = lista[0][1]
    gols_ida_t1 = ida[0][2][0]
    gols_volta_t1 = volta[0][2][1]
    gols_ida_t2 = ida[0][2][1]
    gols_volta_t2 = volta[0][2][0]
    if gols_ida_t1>gols_ida_t2 and gols_volta_t1>gols_volta_t2:
        return {time1:6,time2:0}
    elif gols_ida_t1>gols_ida_t2 and gols_volta_t1<gols_volta_t2:
        return {time1:3,time2:3}
    elif gols_ida_t1<gols_ida_t2 and gols_volta_t1>gols_volta_t2:
        return {time1:3,time2:3}
    elif gols_ida_t1<gols_ida_t2 and gols_volta_t1<gols_volta_t2:
        return {time1:0,time2:6}
    else:
        return {time1:1,time2:1}