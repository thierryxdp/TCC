from collections import OrderedDict

def pontos_por_time(ida_e_volta):
    dict_times = OrderedDict()


    ############# Ida

    patida_ida = ida_e_volta[0]
    time1_ida =  patida_ida[0]
    time2_ida = patida_ida[1]
    placar_ida =  patida_ida[2]
    pontos_time1_ida = 0
    pontos_time2_ida = 0
    if placar_ida[0] == placar_ida[1]:
        pontos_time1_ida = 1
        pontos_time2_ida = 1
    elif  placar_ida[0] > placar_ida[1]:
        pontos_time1_ida = 3
        pontos_time2_ida = 0
    else:
        pontos_time1_ida = 0
        pontos_time2_ida = 3

    if time1_ida in  dict_times: 
        dict_times[time1_ida] += pontos_time1_ida
    else:
        dict_times[time1_ida] = pontos_time1_ida

    if time2_ida in  dict_times: 
        dict_times[time2_ida] += pontos_time2_ida
    else:
        dict_times[time2_ida] = pontos_time2_ida


    partida_volta =  ida_e_volta[1]
    time1_volta =  partida_volta[0]
    time2_volta = partida_volta[1]
    placar_volta =  partida_volta[2]

    ############# Volta

    pontos_time1_volta = 0
    pontos_time2_volta = 0
    if placar_volta[0] == placar_volta[1]:
        pontos_time1_volta = 1
        pontos_time2_volta = 1
    elif  placar_volta[0] > placar_volta[1]:
        pontos_time1_volta = 3
        pontos_time2_volta = 0
    else:
        pontos_time1_volta = 0
        pontos_time2_volta = 3

    if time1_ida in dict_times: 
        dict_times[time1_volta] += pontos_time1_volta
    else:
        dict_times[time1_volta] = pontos_time1_volta

    if time2_volta in  dict_times: 
        dict_times[time2_volta] += pontos_time2_volta
    else:
        dict_times[time2_volta] = pontos_time2_volta

    return dict_times