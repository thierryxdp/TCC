def pontos_por_time(lista):
    time1, time2 = lista[0][0], lista[0][1]
    t1_points, t2_points = 0, 0

    if lista[0][2][0] == lista[0][2][1]:
        t1_points += 1
        t2_points += 1
         
    if lista[1][2][0] == lista[1][2][1]:
        t1_points += 1
        t2_points += 1

    if lista[0][2][0] > lista[0][2][1]:
        t1_points += 3
    
    if lista[1][2][0] < lista[1][2][1]:
        t1_points += 3

    if lista[1][2][0] > lista[1][2][1]:
        t2_points += 3
    
    if lista[0][2][0] < lista[0][2][1]:
        t2_points += 3

    return {time1: t1_points, time2: t2_points}