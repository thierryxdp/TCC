def pontos_por_time(jogos):
    ''' Função que define os pontos da tabela dos times.
    	em caso de Vitoria = 3p
        em caso de Empate = 1p
        em caso de Derrota = 0p
        	list--->dic'''
    time1a = jogos[0][0]
    gl1a = jogos[0][2][0]
    gl2a = jogos[1][2][0]
    time2b = jogos[0][1]
    gl3b = jogos[0][2][1] 
    gl4b = jogos[1][2][1]
  
    
    
    if gl1a>gl3b and gl2a<gl4b:
        return {time1a:3+3 ,time2b:0}
    elif gl1a>gl3b and gl2a<gl4b:
        return {time1a:3 ,time2b:3}
    elif gl1a==gl3b and gl2a==gl4b:
        return {time1a:2 ,time2b:2}
    elif gl1a==gl3b and gl2a<gl4b or gl1a>gl3b and gl2a==gl4b : 
        return {time1a:4 ,time2b:1}


    elif gl1a<gl3b and gl2a>gl4b:
        return {time1a:0 ,time2b:6}
    elif gl1a>gl3b and gl2a<gl4b:
        return {time1a:3 ,time2b:3}
    elif gl1a==gl3b and gl2a==gl4b:
        return {time1a:2 ,time2b:2}
    elif gl1a>gl3b and gl2a==gl4b or gl1a==gl3b and gl2a>gl4b:
        return {time1a:1 ,time2b:4}