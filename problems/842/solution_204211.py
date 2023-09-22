def pontos_primeiro_jogo(lista):
     '''uma função que receba uma lista de dois elementos, onde cada elemento é uma listas e devolve o total do primeiro jogo'''
    # list > int
     primeiro_jogo_time1 =[]
     primeiro_jogo_time2 = []
     primeiro_jogo = lista[0][2]
     if primeiro_jogo[0] > primeiro_jogo[1]:
        primeiro_jogo_time1.append(3)
        primeiro_jogo_time2.append(0)
     elif primeiro_jogo[0] == primeiro_jogo[1]:
        primeiro_jogo_time1.append(1)
        primeiro_jogo_time2.append(1)
     elif primeiro_jogo[0] < primeiro_jogo[1]:
        primeiro_jogo_time1.append(0)
        primeiro_jogo_time2.append(3)
     primeiro_jogo_time_1 = sum(primeiro_jogo_time1)
     primeiro_jogo_time_2 = sum(primeiro_jogo_time2)
     total_primeiro_jogo = [primeiro_jogo_time_1, primeiro_jogo_time_2]
     return total_primeiro_jogo
    
def pontos_segundo_jogo(lista):
     '''uma função que receba uma lista de dois elementos, onde cada elemento é uma listas e devolve o total do segundo jogo'''
    # list > int
     segundo_jogo = lista[1][2]
     segundo_jogo_time1 = []
     segundo_jogo_time2 = []
     if segundo_jogo[0] > segundo_jogo[1]:
        segundo_jogo_time2.append(0)
        segundo_jogo_time1.append(3)
     elif segundo_jogo[0] < segundo_jogo[1]:
        segundo_jogo_time2.append(3)
        segundo_jogo_time1.append(0)
     elif segundo_jogo[0] == segundo_jogo[1]:
        segundo_jogo_time2.append(1)
        segundo_jogo_time1.append(1)
     segundo_jogo_time_1 = sum(segundo_jogo_time1)
     segundo_jogo_time_2 = sum(segundo_jogo_time2)
     total_segundo_jogo = [segundo_jogo_time_1, segundo_jogo_time_2]
     return total_segundo_jogo

def pontos_por_time(lista):
    '''uma função que receba uma lista de dois elementos, onde cada elemento é uma lista e devolta um dicionario com o time e o total de pontos em dois jogos'''
    # list > dic
    jogo1 = pontos_primeiro_jogo(lista)
    jogo2 = pontos_segundo_jogo(lista)
    time1 = jogo1[0] + jogo2[1]
    time2 = jogo1[1] + jogo2[0]
    total1 = time1
    total2 = time2
    res = {lista[0][0]:total1, lista[0][1]:total2}
    return res