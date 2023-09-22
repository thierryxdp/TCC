def pontos_por_time(jogos):
    '''funcao que retorna o mapeament da pontuacao total dos times, 
    ao receber 2 listas com seus respectivos resultados.
    list(list(str,str,list(int,int)), list(str,str,list(int,int))) -> dict'''
    t1_gol1 = jogos[0][2][0]
    t1_gol2 = jogos [1][2][1]
    t2_gol1 = jogos[0][2][1]
    t2_gol2 = jogos[1][2][0]
    result1 = t1_gol1 - t2_gol1
    result2 = t1_gol2 - t2_gol2
    time1 = jogos [0][0]
    time2 = jogos [0][1]
    pontos = {}
    vitoria = 3
    empate = 1
    derrota = 0
    
    if result1 > 0 and result2 > 0:
        pontos[time1]=(vitoria)*2
        pontos[time2]= derrota
        return pontos
    elif result1 > 0 and result2 ==0:
        pontos[time1]=(vitoria)+(empate)
        pontos[time2]= empate
        return pontos
    elif result1 ==0 and result2==0:
        pontos[time1]=(empate)*2
        pontos[time2]= (empate)*2
        return pontos
    elif result1 < 0 and result2 < 0:
        pontos[time1]=derrota
        pontos[time2]= (vitoria)*2
        return pontos
    elif result1 > 0 and result2 < 0 or result1 < 0 and result2 > 0:
        pontos[time1]= vitoria
        pontos[time2]= vitoria
        return pontos
    else: 
        pontos[time1]=(empate)
        pontos[time2]=(empate)+(vitoria)
        return pontos