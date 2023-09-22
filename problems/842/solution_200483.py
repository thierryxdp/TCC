def pontos_por_time(lista):
    """função que define a quantidade de pontos dos dois times;
    lista ->dicionário"""
    time1 = lista[0][0]
    time2 = lista[0][1]
    golstime1p1 = lista[0][2][0]
    golstime1p2 = lista[1][2][1]
    golstime2p1 = lista[0][2][1]
    golstime2p2 = lista[1][2][0]
    pontostime1 = 0
    pontostime2 = 0
    if golstime1p1 > golstime2p1:
        pontostime1 += 3
    if golstime2p1 > golstime1p1:
        pontostime2 += 3
    if golstime1p1 == golstime2p1:
        pontostime1 += 1
        pontostime2 += 1
    if golstime1p2 > golstime2p2:
        pontostime1 += 3
    if golstime2p2 > golstime1p2:
        pontostime2 += 3
    if golstime1p2 == golstime2p2:
        pontostime1 += 1
        pontostime2 += 1
    return {time1:pontostime1, time2:pontostime2}#Start your python function here