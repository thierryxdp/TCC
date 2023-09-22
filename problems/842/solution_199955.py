def pontos_por_time(lista1):
    if lista1[0][2][0]>lista1[0][2][1] and lista1[1][2][1]>lista1[1][2][0]:
        return {lista1[0][0]:6,lista1[0][1]:0}
    elif lista1[0][2][0] == lista1[0][2][1] and lista1[1][2][1]==lista1[1][2][0]:
        return {lista1[0][0]:2,lista1[0][1]:2}
    elif lista1[0][2][0]>lista1[0][2][1] and lista1[1][2][0]>lista1[1][2][1]:
        return {lista1[0][0]:3,lista1[0][1]:3}
    elif lista1[0][2][0]<lista1[0][2][1] and lista1[1][2][1]<lista[1][2][0]:
        return {lista1[0][0]:0,lista1[0][1]:6}
    elif lista1[0][2][0]< lista1[0][2][1] and lista1[1][2][1]> lista1[1][2][0]:
        return {lista1[0][0]:3,lista1[0][1]:3}
    elif lista1[0][2][0]<lista1[0][2][1] and lista1[1][2][1]==lista1[1][2][0]:
        return {lista1[0][0]:1,lista[0][1]:4}
    else:
        return {lista1[0][0]:1,lista1[0][1]:4}