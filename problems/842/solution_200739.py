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
    return  time2