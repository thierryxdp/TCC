def pontos_por_time(lista):
    time1 = 0
    time2 = 0
    if lista[0][2][0] > lista[0][2][1]:
        time1 += 3
    if lista[0][2][0] < lista[0][2][1]:
        time2 += 3
    if lista[0][2][0] == lista[0][2][1]:
        time1 += 1
        time2 += 1
        
    if lista[1][2][1] > lista[1][2][0]:
        time1 += 3
    if lista[1][2][1] < lista[1][2][0]:
        time2 += 3
    if lista[1][2][0] == lista[1][2][1]:
        time1 += 1
        time2 += 1
    
    resultado = {lista[0][0]: time1, lista[0][1]: time2}
    return resultado