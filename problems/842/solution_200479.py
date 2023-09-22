def pontos_por_time(jogo1,jogo2):
    '''Função que recebe uma lista de dois elementos, onde cada elemento é também uma lista e retorne um dicionário cujos mapeamentos são <nome do time> -> <numero total de pontos na fase>; list, list -> dict'''
    jogo1[:1]=time1
    jogo2[:1]=time2
    pontos_t1 = time1[2:3]+time2[2:3]
    pontos_t2 = time1[3:]+time2[3:]
    return {time1:pontos_t1,time2:pontos_t2}