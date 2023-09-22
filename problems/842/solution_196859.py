def pontos_por_time (lista):
    '''
    função que recebe uma lista de dois elementos, onde cada elemento é também uma lista
    que cmpleta, tem informações do número de gols, em dois jogos de futebol entre dois 
    times, no formato: [['time1','time2',[gols1,gols2]],['time2','time1',[gols3,gols4]]]
    lista -> dicionário
    '''
    if lista[0:1][2:3][0:1] > lista[0:1][2:3][1:2] and lista[1:2][2:3][1:2] > lista[1:2][2:3][0:1]:
        return {lista[0:1][0:1]: 6, lista[0:1][1:2]: 0}
    elif lista[0:1][2:3][1:2] > lista[0:1][2:3][0:1] and lista[1:2][2:3][0:1] > lista[1:2][2:3][1:2]:
        return {lista[0:1][1:2]:6, lista[0:1][0:1]:0}
    elif lista[0:1][2:3][0:1] > lista[0:1][2:3][1:2] and lista[1:2][2:3][0:1] == lista[1:2][2:3][1:2]:
        return {lista[0:1][0:1]:4, lista[0:1][1:2]:1}
    elif lista[0:1][2:3][1:2] > lista[0:1][2:3][0:1] and lista[1:2][2:3][1:2] == lista[1:2][2:3][0:1]:
        return {lista[0:1][1:2]:4, lista[0:1][0:1]:1}
    elif lista[0:1][2:3][0:1] > lista[0:1][2:3][1:2] and lista[1:2][2:3][0:1] > lista[1:2][2:3][1:2] or lista[0:1][2:3][0:1] < lista[0:1][2:3][1:2] and lista[1:2][2:3][0:1] < lista[1:2][2:3][1:2]:
        return {lista[0:1][0:1]:3, lista[0:1][1:2]:3}
    else:
        return {lista[0:1][0:1]:3, lista[0:1][1:2]:3}