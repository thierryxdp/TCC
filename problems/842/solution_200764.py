def pontos_por_time(*jogo):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'list-->(list,list) --> dict'

    jogo=list(jogo)

    jogo_ida=jogo[0] or jogo[1] 
    jogo_volta=jogo[1] or jogo[0]
    resultado_ida=jogo[2]
    resultado_volta=jogo[5]
    vitoria=3
    empate=1
    derrota=0