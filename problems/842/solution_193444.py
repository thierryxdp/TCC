def pontos_por_time (lista1, lista2):
    """retorna os pontos dos times. str->str."""
    time1_ida = lista1[0]
    time2_ida = lista1[1]
    gol_ida_time1 = lista1[2]
    gol_ida_time2 = lista1[3]
    time1_ida = time2_volta
    time2_ida = time1_volta
    gol_volta_time1 = lista2[2]
    gol_volta_time2 = lista2[3]
    
    if (gol_ida_time1>gol_ida_time2):
        ponto_ida_time1 = 3
        ponto_ida_time2 = 0
    if (gol_ida_time1==gol_ida_time2):
        ponto_ida_time1 = 1
        ponto_ida_time2 = 1
    if (gol_ida_time2>gol_ida_time1):
        ponto_ida_time2 = 3
        ponto_ida_time1 = 0
    if (gol_volta_time2>gol_volta_time1):
        ponto_volta_time2 = 3
        ponto_volta_time1 = 0
    if (gol_volta_time2==gol_volta_time1):
        ponto_volta_time2 = 1
        ponto_volta_time1 = 1
    if (gol_volta_time1>gol_volta_time2):
        ponto_volta_time1 = 3
        ponto_volta_time2 = 0
        
    total_pontos_time1 = ponto_ida_time1 + ponto_volta_time2
    total_pontos_time2 = ponto_ida_time2 + ponto_volta_time1

    dicionario = {str(time1):total_pontos_time1, str(time2):total_pontos_time2}
    return (dicionario)