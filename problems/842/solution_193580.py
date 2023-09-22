def pontos_por_time(lista1,lista2):
    [timea,timeb,gol_timea_ida, gol_timeb_ida] = lista1
    [timeb,timea,gol_timeb_volta,gol_timea_volta] = lista2
    if (int(gol_timea_ida)>int(gol_timeb_ida)):
        ponto_timea = 3
        ponto_timeb = 0
    if (int(gol_timea_ida)==int(gol_timeb_ida)):
        ponto_timea = 1
        ponto_timeb = 1
    if (int(gol_timea_ida)<int(gol_timeb_ida)):
        ponto_timea = 0
        ponto_timeb = 0
    if (int(gol_timea_volta)>int(gol_timeb_volta)):
        ponto_timea = ponto_timea + 3
        ponto_timeb = ponto_timeb + 0
    if (int(gol_timea_volta)==int(gol_timeb_volta)):
        ponto_timea = ponto_timea + 1
        ponto_timeb = ponto_timeb + 1
    if (int(gol_timea_volta)<int(gol_timeb_volta)):
        ponto_timea = ponto_timea + 0
        ponto_timeb = ponto_timeb + 3
    return {timea: ponto_timea, timeb: ponto_timeb}