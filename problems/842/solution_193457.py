def pontos_por_time(lista):
    '''a partir do nome de 2 times e do placar de um jogo entre eles, retorna a pontuação que o jogo rendeu a cada um deles'''
    nome_do_time=lista[0]
    numero_gols=lista[1]
    if numero_gols[0]>numero_gols[1]:
        return list(nome_do_time[0],'3',nome_do_time[1],'0')
    elif numero_gols[1]>numero_gols[0]:
        return list(nome_do_time[1],'3',,nome_do_time[0],'0')
    elif numero_gols[1]==numero_gols[0]:
        return list(nome_do_time[1],'1',nome_do_time[0],'1')