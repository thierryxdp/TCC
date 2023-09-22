def pontos_por_time(*jogo):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'list-->(list,list) --> dict'

    jogo=list(jogo)
    numero_de_pontos=(0,1,3)

    jogo=[[jogo[0],jogo[1],jogo[2]],[jogo[3],jogo[4],jogo[5]]]

             
    
    time1= jogo[1][1] and jogo[0][0]
    time2= jogo[0][1] and jogo[1][0]
    jogo_ida=jogo[0][2]
    jogo_volta=jogo[1][2]
    
    vitoria=3
    empate=1
    derrota=0
    
    if jogo_ida[0]+jogo_volta[1]>jogo_ida[1]+jogo_volta[0]\
    and jogo_ida > jogo_volta:
         return  jogo