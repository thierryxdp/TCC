def pontos_por_time (lista):
    '''
    função que recebe uma lista de dois elementos, onde cada elemento é também uma lista
    que cmpleta, tem informações do número de gols, em dois jogos de futebol entre dois 
    times, no formato: [['time1','time2',[gols1,gols2]],['time2','time1',[gols3,gols4]]]
    lista -> dicionário
    '''
    lista[0:1] = lista1
    lista[1:2] = lista2
    lista1 = [time1, time2, [gols1, gols2]]
    lista2 = [time2, time1, [gols3, gols4]]
    lista1[2:3] = golsjg1
    lista2[2:3] = golsjg2

    if int(golsjg1[0:1]) > int(golsjg1[1:2]) and int(golsjg2[1:2]) > int(golsjg2[0:1]):
        return {lista1[0:1]: 6, lista1[1:2]: 0}
    elif int(golsjg1[1:2]) > int(golsjg1[0:1]) and int(golsjg2[0:1]) > int(golsjg2[1:2]):
        return {lista1[1:2]:6, lista1[0:1]:0}
    elif int(golsjg1[0:1]) > int(golsjg1[1:2]) and int(golsjg2[0:1]) == int(golsjg2[1:2]):
        return {lista1[0:1]:4, lista1[1:2]:1}
    elif int(golsjg1[1:2]) > int(golsjg1[0:1]) and int(golsjg2[1:2]) == int(golsjg2[0:1]):
        return {lista1[1:2]:4, lista1[0:1]:1}
    elif int(golsjg1[0:1]) > int(golsjg1[1:2]) and int(golsjg2[0:1]) > int(golsjg2[1:2]) or int(golsjg1[0:1]) < int(golsjg1[1:2]) and int(golsjg2[0:1]) < int(golsjg2[1:2]):
        return {lista1[0:1]:3, lista1[1:2]:3}
    else:
        return {lista1[0:1]:2, lista1[1:2]:2}