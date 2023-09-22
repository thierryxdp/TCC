def pontos_por_time (partida1,partida2):
    '''
    essa função recebe uma lista de 2 elementos, onde cada elemento é uma lista; e retorna um dicionário com o nome do time e seus respectivos pontos adquiridos nas partidas 
    '''
    return {partida1[0]: partida1[2][0] + partida2[2][1], partida2[0]: partida1[2][1] + partida2[2][0]}