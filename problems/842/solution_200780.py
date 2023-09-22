def pontos_por_time(*jogo):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'list-->(list,list) --> dict'

    jogo=list(jogo)

    jogo_ida=jogo[0][0] 
    jogo_volta=jogo[0][1]
    
    gols_jogo_ida=jogo_ida[2]
    gols_jogo_volta=jogo_volta[2]
    
    vitoria=3
    empate=1
    derrota=0
    
    return jogo_ida[2]