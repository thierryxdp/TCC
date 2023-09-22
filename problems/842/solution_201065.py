def pontos_por_time(lista):
    '''dado dois times e seus números de gol em cada partida, retorna um dicionário com os times e suas pontuações;
    list -> dic'''
    time1 = lista[0][0]
    time2 = lista[0][1]
    gol1 = lista[0][2][0]
    gol2 = lista[0][2][1]
    if gol1 > gol2:
        ponto1 = 3
        ponto2 = 0
    elif gol1 == gol2:
        ponto1 = 1
        ponto2 = 1
    else:
        ponto1= 0
        ponto2 = 3
        
    if time1 == lista[1][0]:
        gol1 = lista[1][2][0]
        gol2 = lista[1][2][1]
    elif time1 == lista[1][1]:
        gol1 = lista[1][2][1]
        gol2 = lista[1][2][0]
       
    if gol1 > gol2:
        ponto1 += 3
    elif gol1 == gol2:
        ponto1 += 1
        ponto2 += 1
    else:
        ponto2 += 3
        
    resultado = {time1:ponto1, time2:ponto2}
        
    return resultado