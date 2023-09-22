def pontos_por_time(jogos):
    '''retorna o numero total de pontos de cada time dadas duas listas dos jogos. list,list->dict.'''
    nome_time1 = jogo_ida [0] and jogo_volta[1]
    nome_time2 = jogo_ida[1] and jogo_volta [0]
    if jogo_ida[2][0]> jogo_ida [2][1] and jogo_volta[2][0]< jogo_volta[2][1]:
        return {'nome_time1':6, 'nome_time2':0}
    elif jogo_ida [2][0]< jogo_ida [2][1] and jogo_volta[2][0]> jogo_volta[2][1]:
        return {'nome_time1':0, 'nome_time2':6}
    elif jogo_ida [2][0]> jogo_ida [2][1] and jogo_volta[2][0]> jogo_volta[2][1]:
        return {'nome_time1':3, 'nome_time2':3}  
    elif jogo_ida [2][0]< jogo_ida [2][1] and jogo_volta[2][0]< jogo_volta[2][1]:
        return {'nome_time1':3, 'nome_time2':3}
    elif jogo_ida [2][0]== jogo_ida [2][1] and jogo_volta[2][0]< jogo_volta[2][1]:
        return {'nome_time1':4, 'nome_time2':1}
    elif jogo_ida [2][0]< jogo_ida [2][1] and jogo_volta[2][0]== jogo_volta[2][1]:
        return {'nome_time1':1, 'nome_time2':4}
    else:
        return {'nome_time1':1, 'nome_time2':1}