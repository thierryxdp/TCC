def pontos_por_time(lista):
    lista1 = lista[0]
    lista2 = lista[1]
    gols_ida = lista1[2]
    gols_volta = lista2[2]
    if (gols_ida[0]>gols_ida[1]):
        ponto_time1 = 3
        ponto_time2 = 0
    if (gols_ida[0]==gols_ida[1]):
        ponto_time1 = 1
        ponto_time2 = 1
    if (gols_ida[0]<gols_ida[1]):
        ponto_time1 = 0
        ponto_time2 = 3
    if (gols_volta[0]>gols_volta[1]):
        ponto_time2 = ponto_time2 + 3
        ponto_time1 = ponto_time1
    if (gols_volta[0]==gols_volta[1]):
        ponto_time2 = ponto_time2 + 1
        ponto_time1 = ponto_time1 + 1
    if (gols_volta[0]<gols_volta[1]):
        ponto_time1 = ponto_time1 + 3
        ponto_time2 = ponto_time2 
    return {str(lista1[0]):ponto_time1, str(lista2[0]): ponto_time2}