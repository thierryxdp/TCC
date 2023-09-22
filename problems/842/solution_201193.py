def pontos_por_time(lista):
    ''' funcao que recebe uma lista com informaçoes do numero de gols em dois jogos de futebol entre dois times, e retorne uma diciionario com o numero total de pontos que cada time fez na fase:
    list -> dict'''
    time1 = lista[0]
    time2 = lista[1]
    pontos1 = lista[2] [0] + lista[5] [1]
    pontos2 = lista[2] [1] + lista[5] [0]
    return {time1: pontos1 , time2:pontos2}