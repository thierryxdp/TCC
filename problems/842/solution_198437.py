def pontos_por_time(lista):
    time1 = lista[0][0]
    time2 = lista[0][1]
    dic = {}
    pontos1 = 0
    pontos2 = 0
    
    if lista[0][2][0] > lista[0][2][1]:
        pontos1 = pontos1 + 3
        #dic[time1] = 3
    if lista[0][2][0] = lista[0][2][1]:
        pontos1 = pontos1 + 1
        pontos2 = pontos2 + 1
        #dic[time1] = 1
        #dic[time2] = 1
    if lista[1][2][0] < lista[1][2][1]:
        pontos2 = pontos2 + 3
        #dic[time2] = 3
    
    if lista[1][2][0] > lista[1][2][1]:
        pontos1 = pontos1 + 3
    if lista[1][2][0] = lista[1][2][1]:
        pontos1 = pontos1 + 1
        pontos2 = pontos2 + 1
    if lista[1][2][0] < lista[1][2][1]:
        pontos2 = pontos2 + 3
        
    dic[time1] = pontos1
    dic[time2] = pontos2
    
    return dic