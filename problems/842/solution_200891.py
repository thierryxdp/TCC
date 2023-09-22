def pontos_por_time(*jogo):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'list-->(list,list) --> dict'

    jogo=list(jogo)

    jogo_ida=jogo[0][0] 
    jogo_volta=jogo[0][1]
    jogo_ida=list(jogo_ida)
    
    gols_jogo_ida=jogo_ida
    return jogo_ida