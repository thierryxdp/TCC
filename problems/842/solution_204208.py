def pontos_por_time(lista):
    '''uma função que receba uma lista de dois elementos, onde cada elemento é uma lista e devolta um dicionario com o time e o total de pontos em dois jogos'''
    # list > dic
    primeiro_jogo = lista[0][2]
    segundo_jogo = lista[1][2]
    primeiro_jogo_time1 = []
    primeiro_jogo_time2 = []
    segundo_jogo_time1 = []
    segundo_jogo_time2 = []
    if primeiro_jogo[0] > primeiro_jogo[1]:
        primeiro_jogo_time1.append(3)
        primeiro_jogo_time2.append(0)
    elif primeiro_jogo[0] == primeiro_jogo[1]:
        primeiro_jogo_time1.append(1)
        primeiro_jogo_time2.append(1)
    elif primeiro_jogo[0] < primeiro_jogo[1]:
        primeiro_jogo_time1.append(0)
        primeiro_jogo_time2.append(3)
    elif segundo_jogo[0] > segundo_jogo[1]:
        segundo_jogo_time2.append(0)
        segundo_jogo_time1.append(3)
    elif segundo_jogo[0] < segundo_jogo[1]:
        segundo_jogo_time2.append(3)
        segundo_jogo_time1.append(0)
    elif segundo_jogo[0] == segundo_jogo[1]:
        segundo_jogo_time2.append(1)
        segundo_jogo_time1.append(1)
    primeiro_time = primeiro_jogo_time1 + segundo_jogo_time1
    segundo_time = primeiro_jogo_time2 + segundo_jogo_time2
    total_primeiro_time = sum(primeiro_time)
    total_segundo_time = sum(segundo_time)
    res = {lista[0][0]:total_primeiro_time, lista[0][1]:total_segundo_time}
    return res