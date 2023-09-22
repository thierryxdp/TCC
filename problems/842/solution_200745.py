def pontos_por_time(*jogo):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'list-->(list,list) --> dict'

    jogo=list(jogo)
    
    
    jogo_ida=jogo[0][0] 
    jogo_volta=jogo[0][1]
    
    vitoria=3
    empate=1
    derrota=0
    numero_de_pontos={vitoria:3, empate:1, derrota:0}

    time1 = jogo_ida[0] or jogo_volta[1]
    time2 = jogo_volta[0] or jogo_ida[1]
        
    return  jogo_volta[1]