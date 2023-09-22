def pontos_por_time(jogo1,jogo2):
    '''retorna um dicionario dados os resultados de dois jogos'''

    return {jogo1[0]:jogo1[2][0] + jogo2[2][0], jogo1[1]:jogo1[2][1] + jogo2[2][1]}