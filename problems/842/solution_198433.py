def pontos_por_time(lista):
    dic = {'Cormengo': 0, 'Flamínthians': 0}
    
    if lista[0][2][0] > lista[0][2][1]:
        dic['Cormengo'] = dic['Cormengo'] + 3
    elif lista[0][2][0] = lista[0][2][1]:
        dic['Cormengo'] = dic['Cormengo'] + 1
        dic['Flamínthians'] = dic['Flamínthians'] + 1
    elif lista[1][2][0] < lista[1][2][1]:
        dic['Flamínthians'] = dic['Flamínthians'] + 3
    
    if lista[1][2][0] > lista[1][2][1]:
        dic['Cormengo'] = dic['Cormengo'] + 3
    elif lista[1][2][0] = lista[1][2][1]:
        dic['Cormengo'] = dic['Cormengo'] + 1
        dic['Flamínthians'] = dic['Flamínthians'] + 1
    elif lista[1][2][0] < lista[1][2][1]:
        dic['Flamínthians'] = dic['Flamínthians'] + 3
    
    return dic