def pontos_por_time(jogos):
    '''lista lista > dict
    Recebe duas listas que representam 2 jogos jogados por exatamente 2 times. Em um jogo um time jogará em casa e no outro, jogará fora de casa, a ordem em que são escritos é o que define esse fator.
    Retorna os pontos acumulados nos 2 jogos pelos 2 times, levando em conta que uma vitória dá 3 pontos, um empate dá 1 ponto e uma derrota não dá pontos.
    Casos de teste: pontos_por_time([['fla','cor',[2,0]], ['cor','fla',[1,1]]]) == {'cor' : 1, 'fla': 4}
    pontos_por_time([['real','liv',[4,0]], ['liv','real',[1,3]]]) == {'liv' : 0, 'real' : 6} 
    pontos_por_time ([['river','boca',[2,2]], ['boca','river',[0,0]]]) == {'boca' : 2, 'river' : 2} '''

    jogo1 = jogos[0]
    jogo2 = jogos[1]
    
    t1 = jogo1[0]
    t2 = jogo1[1]
    
    gol1_jg1 = jogo1[2][0]
    gol2_jg1 = jogo1[2][1]
    gol1_jg2 = jogo2[2][0]
    gol2_jg2 = jogo2[2][1]
    
    ptsjogo1 = pts([gol1_jg1, gol2_jg1])
    ptsjogo2 = pts([gol1_jg2, gol2_jg2])
    
    ptstime1 = ptsjogo1[0] + ptsjogo2[1]
    ptstime2 = ptsjogo1[1] + ptsjogo2[0]
    
    return {t2 : ptstime2,
            t1 : ptstime1}