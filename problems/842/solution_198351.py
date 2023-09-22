def pontos_por_time(a):
    dicionario1 = {'Cormengo':4, 'Flamínthians':1}
    dicionario2 = {'Cormengo':6, 'Flamínthians':0}
    dicionario3 = {'Cormengo':1, 'Flamínthians':4}
    dicionario4 = {'Cormengo':0, 'Flamínthians':6}
    dicionario5 = {'Cormengo':2, 'Flamínthians':2}
    if((((a[0][2][0])> (a[0][2][1])) and (a[1][2][0])== (a[1][2][1])) or (((a[0][2][0])== (a[0][2][1])) and (a[1][2][0])> (a[1][2][1]))):
        return dicionario1
    elif(((a[0][2][0])> (a[0][2][1])) and (a[1][2][0])> (a[1][2][1])):
        return dicionario2
    elif((((a[0][2][0])< (a[0][2][1])) and (a[1][2][0])== (a[1][2][1])) or (((a[0][2][0])==(a[0][2][1])) and (a[1][2][0])<(a[1][2][1]))):
        return dicionario3
    elif(((a[0][2][0])< (a[0][2][1])) and (a[1][2][0])< (a[1][2][1])):
        return dicionario4
    else:
        return dicionario5