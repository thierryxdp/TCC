def pontos_por_time(*jogo):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'list-->(list,list) --> dict'

    jogo=list(jogo)
    numero_de_pontos=(0,1,3)

    time1= jogo[1] 
    time2= jogo[0]
    jogo_ida=jogo[0]
    jogo_volta=jogo[1]
    
    vitoria=3
    empate=1
    derrota=0
    return  jogo