def pontos_por_time(jogo1,jogo2):
    '''Função que recebe uma lista de dois elementos, onde cada elemento é também uma lista e retorne um dicionário cujos mapeamentos são <nome do time> -> <numero total de pontos na fase>; list, list -> dict'''
    pontos_t1 = jogo1[2][0]+jogo2[2][1]
    pontos_t2 = jogo2[2][1]+jogo2[2][0]
    return {jogo1[0]:pontos_t1, jogo2[0]:pontos_t2}