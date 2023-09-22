def pontos_por_time(jogos):
    '''retorna o numero total de pontos de cada time dadas duas listas dos jogos. list,list->dict.'''
    jogos = [[jogo_ida], [jogo_volta]]
    jogo_ida = [nome_time1, nome_time2,[num_pontos1,num_pontos2]]
    jogo_volta = [nome_time2, nome_time1,[num_pontos2,num_pontos1]]
    nome_time1 = jogo_ida [0]
    nome_time2 = jogo_volta[0]
    num_pontos1 = jogo_ida[2][0]+ jogo_volta[2][1]
    num_pontos2 = jogo_ida[2][1]+ jogo_volta[2][0]
    if num_pontos1> num_pontos2:
        return {'nome_time1':6, 'nome_time2':0}
    elif num_pontos1< num_pontos2:
        return {'nome_time1':0, 'nome_time2':6}
    elif num_pontos1> num_pontos2:
        return {'nome_time1':3, 'nome_time2':3}