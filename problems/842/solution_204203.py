def pontos_por_time(lista):
    '''uma função que receba uma lista de dois elementos, onde cada elemento é uma lista e devolta um dicionario com o time e o total de pontos em dois jogos'''
    # list > dic
    lista1 = lista[0][2]
    lista2 = lista[1][2]
    if lista1[0] > lista1[1]:
        primeiro_jogo_time1 = [lista1[0]] #primeiro time
        primeiro_jogo_time2 = [lista1[1]] #segundo time
    elif lista1[0] == lista1[1]:
        primeiro_jogo_time1 = [lista1[0]] #primeiro time
        primeiro_jogo_time2 = [lista1[1]] #segundo time
    elif lista2[0] > lista2[1]:
        segundo_jogo_time2 = [lista2[0]] #segundo time
        segundo_jogo_time1 = [lista2[1]] #primeiro time
    elif lista2[0] == lista2[1]:
        segundo_jogo_time2 = [lista2[0]] #segundo time
        segundo_jogo_time1 = [lista2[1]] #primeiro time
    primeiro_time = primeiro_jogo_time1 + segundo_jogo_time1
    segundo_time = primeiro_jogo_time2 + segundo_jogo_time2
    total_primeiro_time = sum(primeiro_time)
    total_segundo_time = sum(segundo_time)
    res = {lista[0][0]:primeiro_time, lista[0][1]:segundo_time}
    return res