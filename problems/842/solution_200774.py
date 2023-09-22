def pontos_por_time(*jogo):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'list-->(list,list) --> dict'

    jogo=list(jogo)

    jogo_ida=jogo[0][0] 
    jogo_volta=jogo[0][1]
    
    gols_jogo_ida=jogo[0][2]
    gols_jogo_volta=jogo[0][5]
    
    time1=jogo_ida[0]
    time2=jogo_volta[0]
    return time1
    
    
    
    return jogo_ida