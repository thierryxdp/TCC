def pontos_por_time(lista):
    time1 = lista[0][0]
    time2 = lista[0][1]
    placar1 = lista[0][2]    
    placar2 = lista[1][2][::-1]
    a = placar1.index(max(placar1))
    b = placar2.index(max(placar2))
    ganhadores = {time1:0, time2:1}