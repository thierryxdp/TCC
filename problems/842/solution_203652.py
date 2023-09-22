def pontos_por_time(jogos):
    '''retorna um dicionario dados os resultados de dois jogos'''
  
    return {jogos[0][0]:jogos[0][2][0] + jogos[1][2][1], jogos[0][1]:jogos[0][2][1] + jogos[1][2][0]}