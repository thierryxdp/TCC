def pontos_por_time(*jogo):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'list-->(list,list) --> dict'

    jogo=list(jogo)

    jogo_ida=jogo[0],jogo[1] 
    jogo_volta=jogo[1],jogo[0]
    resultado_ida=jogo[2]
    resultado_volta=jogo[5]
    vitoria=3
    empate=1
    derrota=0
    numero_de_pontos={vitoria:3, empate:1, derrota:0}

    time1 = jogo_ida[0] or jogo_volta[1]
    time2 = jogo_volta[0] or jogo_ida[1]
    gols_time1_ida=jogo[2][0]
    gols_time1_volta=jogo[5][1]
    gols_time2_ida=jogo[2][1]
    gols_time2_volta=jogo[5][0]
    numero_de_pontos=dict(numero_de_pontos)
    numero_de_pontos={'time1':time1, 'resultado1':vitoria,\
          'resultado2':empate,'resultado3':derrota,\
          'time2':time2, 'resultado4':2*vitoria,\
          'resultado5':2*empate,'resultado6':2*derrota}
          
           
    return  numero_de_pontos['time1':'resultado4','time2':'resultado6']