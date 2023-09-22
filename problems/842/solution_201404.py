def pontos_por_time(lista):
    #total de pontos
    Tt1 = 0
    Tt2 = 0
    #Primeiro jogo
    ponto_t1 = lista[0][2][0]
    ponto_t2 = lista[0][2][1]
    #Segundo jogo
    Ponto_t1 = lista[1][2][1]
    Ponto_t2 = lista[1][2][0]
    if ponto_t1 > ponto_t2:
        Tt1 += 3
    if ponto_t1 < ponto_t2:
        Tt2 += 3
    if ponto_t1 == ponto_t2:
        Tt1 += 1
        Tt2 += 1
    if Ponto_t1 > Ponto_t2:
        Tt1 += 3
    if Ponto_t1 < Ponto_t2:
        Tt2 += 3
    if Ponto_t1 == Ponto_t2:
        Tt1 += 1
        Tt2 += 1
    return {lista[0][0]:Tt1,lista[0][1]:Tt2}