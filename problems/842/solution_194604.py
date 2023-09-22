def pontos_por_time(lista1,lista2):
    if (lista1[3]>lista1[4]):
        ponto_time1 = 3
        ponto_time2 = 0
    if (lista1[3]==lista1[4]):
        ponto_time1 = 1
        ponto_time2 = 1
    if (lista1[3]<lista1[4]):
        ponto_time1 = 0
        ponto_time2 = 3
    if (lista2[3]>lista2[4]):
        ponto_time2 = ponto_time2 + 3
        ponto_time1 = ponto_time1
    if (lista2[3]==lista2[4]):
        ponto_time2 = ponto_time2 + 1
        ponto_time1 = ponto_time1 + 1
    if (lista2[3]<lista2[4]):
        ponto_time1 = ponto_time1 + 3
        ponto_time2 = ponto_time2 
    return {str(lista1[0]):ponto_time1, str(lista2[0]): ponto_time2}