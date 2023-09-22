def pontos_por_time(a):
    dicionario1 = {a[0][0]:4, a[0][1]:1}
    dicionario2 = {a[0][0]:6, a[0][1]:0}
    dicionario3 = {a[0][0]:1, a[0][1]:4}
    dicionario4 = {a[0][0]:0, a[0][1]:6}
    dicionario5 = {a[0][0]:2, a[0][1]:2}
    dicionario6 = {a[0][0]:3, a[0][1]:3}
    if((((a[0][2][0])> (a[0][2][1])) and (a[1][2][0])== (a[1][2][1])) or (((a[0][2][0])== (a[0][2][1])) and (a[1][2][0])< (a[1][2][1]))):
        return dicionario1
    elif(((a[0][2][0])> (a[0][2][1])) and (a[1][2][0])< (a[1][2][1])):
        return dicionario2
    elif((((a[0][2][0])< (a[0][2][1])) and (a[1][2][0])== (a[1][2][1])) or (((a[0][2][0])==(a[0][2][1])) and (a[1][2][0])>(a[1][2][1]))):
        return dicionario3
    elif(((a[0][2][0])< (a[0][2][1])) and (a[1][2][0])> (a[1][2][1])):
        return dicionario4
    elif(((a[0][2][0])== (a[0][2][1])) and (a[1][2][0])== (a[1][2][1])):
        return dicionario5
    else:
        return dicionario6