def pontos_por_time(jogo1,jogo2):
    '''Função que recebe uma lista de dois elementos, onde cada elemento é também uma lista e retorne um dicionário cujos mapeamentos são <nome do time> -> <numero total de pontos na fase>; list, list -> dict'''
    pontos_t1=jogo1[2:3]+jogo2[2:3]
    pontos_t2=jogo1[3:]+jogo2[3:]
    return {jogo1[:1]:pontos_t1,jogo2[1:2]:pontos_t2}