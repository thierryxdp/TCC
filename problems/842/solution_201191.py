def pontos_por_time(lista):
    '''funcao que recebe uma lista com informacoes do numero de gols de cada time em dois jogos de futebol e retorna um dicionario  com oo numero total de pontos por times na fase;
    list -> dict'''
    pontos1 = (lista[2][0]) + (lista[5][1])
    pontos2 = int(lista[2][1]) + int(lista[5][0])
    return {lista[0]:pontos1 , lista[1]: pontos2}