def pontos_por_time(*jogo):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'list-->(list,list) --> dict'

    jogo=list(jogo)

    jogo_ida=jogo[0][0] 
    jogo_volta=jogo[0][1]
    
    gols_jogo_ida=jogo_ida[2]
    gols_jogo_volta=jogo_volta[2]
    
    time1=jogo_ida[0] or jogo_volta[1]
    time2=jogo_ida[1] or jogo_volta[0]
    
    vitoria=3
    empate=1
    derrota=0
    numero_de_pontos={'timeA':time1,'timeB':time2,'resultado_1':vitoria,
                      'resultado_2':empate,'resultado_3':derrota,
                      'resultado_4':2*vitoria,'resultado_5':2*empate,}
    if gols_jogo_ida > gols_jogo_volta:
        return {time1:6,time2:0}
    elif gols_jogo_ida < gols_jogo_volta:
    	return {time2:6,time1:0}