def pontos_por_time (jogo1, jogo2):
    '''
    essa função recebe uma lista de 2 elementos, onde cada elemento é uma lista; e retorna um dicionário com o nome do time e seus respectivos pontos adquiridos nas partidas 
    '''
    return {jogo1[0]:jogo1[2][0] + jogo2[2][1], jogo2[0]:jogo1[2][1] + jogo2[2][0]}