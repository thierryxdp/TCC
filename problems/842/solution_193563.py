def pontos_por_time(lista):
    '''dada uma lista formada por duas outras listas contendo o numero de gols de cada time em dois jogos, no formato: [<time1>, <time2>, [<gols_time1>, <gols_time2>]], retorna um dicionario com os pontos de cada time nessa fase; lista -> dicionario'''
    time1 = lista[0][0]
    time2 = lista[0][1]
    fase = {time1:0,time2:0}
    

    if lista[0][2][0] > lista[0][2][1]:
        fase[time1] += 3
        
    if lista[0][2][0] < lista[0][2][1]:
        fase[time2] += 3
        
    if lista[0][2][0] == lista[0][2][1]:
        fase[time1] += 1
        fase[time2] += 1
        
    if lista[1][2][0] < lista[1][2][1]:
        fase[time1] += 3
        
    if lista[1][2][0] > lista[1][2][1]:
        fase[time2] += 3

    if lista[1][2][0] == lista[1][2][1]:
        fase[time2] += 1
        fase[time1] += 1
    return fase