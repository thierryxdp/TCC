def pontos_por_time(lista):
    """Função que recebe uma lista com dois elemantos onde cada elemento tambem é uma lista,
    que representa 2 times e 2 jogos com os respectivos resultados de cada um dos jogos,
    e retorna um dicionario com o nome de cada um dos times e suas pontuações referentes aos 2 confrontos;
    list-->dict"""
    [lista1,lista2] = lista
    [time1,time2,[placar1,placar2]] = lista1 
    [time2,time1,[placar3,placar4]] = lista2 
    lista1[2][0] = placar1 
    lista1[2][1] = placar2 
    lista2[2][0] = placar3
    lista2[2][1] = placar4
    lista1[0] = time1
    lista2[0] = time2 
    
    if placar1 > placar2 and placar3 < placar4:
        return {time1:6, time2:0}
    elif placar1 < placar2 and placar3 > placar4:
        return {time1:0, time2:6}
    elif placar1 > placar2 and placar3 > placar4:
        return {time1:3, time2:3}
    elif placar1 < placar2 and placar3 < placar4:
        return {time1:3, time2:3}
    elif  placar1 > placar2 and placar3 == placar4:
        return {time1:4, time2:1}
    elif  placar1 < placar2 and placar3 == placar4:
        return {time1:1, time2:4}
    elif placar1 == placar2 and placar3 > placar4:
        return {time1:1, time2:4}
    elif placar1 == placar2 and placar3 < placar4:
        return {time1:4, time2:1}
    elif placar1 == placar2 and placar3 == placar4:
        return {time1:2, time2:2}
    else:
        return {time1:1, time2:1}