#primeiro_jogo
def pontos_primeiro_jogo(lista):
     '''uma função que receba uma lista de dois elementos, onde cada elemento é uma lista e devolta um dicionario com o time e o total de pontos em dois jogos'''
    # list > int
    primeiro_jogo = lista[0][2]
    primeiro_jogo_time1 = []
    primeiro_jogo_time2 = []
    if primeiro_jogo[0] > primeiro_jogo[1]:
        primeiro_jogo_time1.append(3)
        primeiro_jogo_time2.append(0)
    elif primeiro_jogo[0] == primeiro_jogo[1]:
        primeiro_jogo_time1.append(1)
        primeiro_jogo_time2.append(1)
    elif primeiro_jogo[0] < primeiro_jogo[1]:
        primeiro_jogo_time1.append(0)
        primeiro_jogo_time2.append(3)
    primeiro_time = primeiro_jogo_time1 + segundo_jogo_time1
    total_primeiro_time = sum(primeiro_time)
    return total_primeiro_time
def pontos_segundo_jogo(lista):
     '''uma função que receba uma lista de dois elementos, onde cada elemento é uma lista e devolta um dicionario com o time e o total de pontos em dois jogos'''
    # list > int
    segundo_jogo = lista[1][2]
    segundo_jogo_time1 = []
    segundo_jogo_time2 = []
    elif segundo_jogo[0] > segundo_jogo[1]:
        segundo_jogo_time2.append(0)
        segundo_jogo_time1.append(3)
    elif segundo_jogo[0] < segundo_jogo[1]:
        segundo_jogo_time2.append(3)
        segundo_jogo_time1.append(0)
    elif segundo_jogo[0] == segundo_jogo[1]:
        segundo_jogo_time2.append(1)
        segundo_jogo_time1.append(1)
    segundo_time = primeiro_jogo_time2 + segundo_jogo_time2
    total_segundo_time = sum(segundo_time)
    return total_segundo_time

def pontos_por_time(lista):
    '''uma função que receba uma lista de dois elementos, onde cada elemento é uma lista e devolta um dicionario com o time e o total de pontos em dois jogos'''
    # list > dic
    res = {lista[0][0]:pontos_primeiro_jogo(lista), lista[0][1]:pontos_segundo_jogo(lista)}
    return res