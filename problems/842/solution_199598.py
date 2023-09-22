def pontos_por_time():
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'dict(str,list),'

    jogo_ida = dict()
    jogo_ida = ['jogo_ida[0]', 'jogo_ida[1]',jogo_ida[2]]
    jogo_volta = ['jogo_volta[0]', 'jogo_volta[1]', jogo_volta[2]]

    jogo_ida[0] = time1

    jogo_ida[1] = time2

    jogo_volta[0] = time2

    jogo_volta[1] = time1

    jogo_ida[2][0] = gol_time_1
    jogo_ida[2][1] = gol_time_2

    jogo_volta[2][0]= gol_time_2
    jogo_volta[2][1]= gol_time_1

    if   jogo_ida[2][0] > jogo_ida[2][1] and jogo_volta[2][1] > jogo_volta[2][0]:
         return resultado[time1]==6, resultado[time2]==0