def pontos_por_time(lista):
    pt1=pontost1j1+pontost1j2
    pt2=pontost2j1+pontost2j2
    desempenho = {lista[1][0]:pt1,lista[1][1]:pt2}
    if lista[0][2][0]>lista[0][2][1]:
           pontost1j1 = 3
           pontost2j1 = 0
    if lista[0][2][0]==lista[0][2][1]:
           pontost1j1  = 1
           pontost2j1  = 1  
    if lista[0][2][0]<lista[0][2][1]:
           pontost1j1 = 0
           pontost2j1 = 3
    if lista[1][2][0]>lista[1][2][1]:
           pontost1j2 = 3
           pontost2j2 = 0
    if lista[1][2][0]==lista[1][2][1]:
           pontost1j2 = 1
           pontost2j2 = 1
    if lista[1][2][0]<lista[1][2][1]:
           pontost1j2 = 0
           pontost2j2 = 0 
    return desempenho