def pontos_por_time(jogos):
    '''calcula e retorna o número total de pontos de cada time dadas duas listas respectivas aos dois jogos jogados. Sendo list,list-->dict.'''
    jogos = [[jogo_ida],[jogo_volta]]
    jogo_ida = [nome_time1, nome_time2,[num_pontos1, num_pontos2]]
    jogo_volta = [nome_time2, nome_time1,[num_pontos3, num_pontos4]]
    jogo_ida[2][0]= num_pontos1
    jogo_ida[2][1]= num_pontos2
    jogo_volta[2][0]= num_pontos3
    jogo_volta[2][1]= num_pontos4
    if (num_pontos1 + num_pontos4) > (num_pontos2 + num_pontos3):
        return {'nome_time1':6, 'nome_time2':0}
    elif (num_pontos1 + num_pontos4) < (num_pontos2 + num_pontos3):
        return {'nome_time1':0, 'nome_time2':6}
    elif (num_pontos1 > num_pontos2) and (num_pontos3 > num_pontos4) or (num_pontos1 < num_pontos2) and (num_pontos3 < num_pontos4):
        return {'nome_time1':3, 'nome_time2':3}
    elif (num_pontos1 == num_pontos4) and (num_pontos2 < num_pontos3):
        return {'nome_time1':4, 'nome_time2':1}
    elif (num_pontos1 < num_pontos4) and (num_pontos2 == num_pontos3):
        return {'nome_time1':1, 'nome_time2':4}
    else:
        return {'nome_time1':1, 'nome_time2':1}