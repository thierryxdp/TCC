def pontos_por_time(jogo1,jogo2):
    '''Função que receba uma lista de dois elementos, onde cada elemento é uma lista. A lista completa tem informações do número de gols em dois jogos de futebol entre dois times, assim, a função retorna um dicionário cujos mapeamentos são <nome do time> -> <numero total de pontos na fase>; list, list -> dict'''
    
    nome_t1=jogo1[0]
    nome_t2=jogo2[0]
    pontos_t1 = jogo1[2][0] + jogo2[2][1] == 3
    pontos_t2 = jogo1[2][1] + jogo2[2][0] == 3
    
    return {nome_t1:pontos_t1, nome_t2:pontos_t2}