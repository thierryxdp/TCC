def pontos_por_time(lista):
    '''funcao que recebe uma lista com informacoes do numero de gols de cada time em dois jogos de futebol e retorna um dicionario  com oo numero total de pontos por times na fase;
    list -> dict'''
    pontosC = lista[2][0] + lista[5][1]
    pontosF = lista[2][1] + lista[5][0]
    return {lista[0]:pontosC , lista[1]: pontosF}