def pontos_por_time([lista1, lista2]):
    """função que retorna a pontuação após o término da rodada"""
    numero_de_gols_1 = lista1[2]
    numero_de_gols_2 = lista2[2]
    gol_time_a_ida = numero_de_gols_1[0]
    gol_time_b_ida = numero_de_gols_1[1]
    gol_time_a_volta = numero_de_gols_2[0]
    gol_time_b_volta = numero_de_gols_2[1]
    saldo_a = gol_time_a_ida + gol_time_a_volta
    saldo_b = gol_time_b_ida + gol_time_b_volta
    time_a = lista1[0]
    time_b = lista1[1]
    if gol_time_a_ida > gol_time_b_ida and gol_time_a_volta > gol_time_b_volta:
        return {time_a : 6, time_b : 0}
    if gol_time_a_ida > gol_time_b_ida and gol_time_a_volta == gol_time_b_volta:
        return {time_a : 4, time_b : 1}
    if gol_time_a_ida > gol_time_b_ida and gol_time_a_volta < gol_time_b_volta:
        return {time_a : 3, time_b : 3}
    if gol_time_a_ida == gol_time_b_ida and gol_time_a_volta > gol_time_b_volta:
        return {time_a : 4, time_b : 1}
    if gol_time_a_ida == gol_time_b_ida and gol_time_a_volta < gol_time_b_volta:
        return {time_a : 1, time_b : 4}
    if gol_time_a_ida == gol_time_b_ida and gol_time_a_volta == gol_time_b_volta:
        return {time_a : 2, time_b : 2}
    if gol_time_a_ida < gol_time_b_ida and gol_time_a_volta > gol_time_b_volta:
        return {time_a : 3, time_b : 3}
    if gol_time_a_ida < gol_time_b_ida and gol_time_a_volta < gol_time_b_volta:
        return {time_a : 0, time_b : 6}
    if gol_time_a_ida < gol_time_b_ida and gol_time_a_volta == gol_time_b_volta:
        return {time_a : 1, time_b : 4}