def pts(ls):
    ''' int int > lista
    Dada uma lista com 2 inteiros que representam gols, calcula o número de pontos que um time ganharia de acordo com os gols.
    Caso um seja maior que o outro, o maior número de gols ganhará 3 pontos e o menor não ganhará nada, caso sejam iguais, cada um ganhará um ponto
    Casos de teste: pts([3,3]) == [1,1]
    pts([1,0]) == [3,0]
    pts([2,4]) == [0,3] '''
    g1 = ls[0]
    g2 = ls[1]
    if g1>g2:
        d = [3,0]
    if g1==g2:
        d = [1,1]
    if g1<g2:
        d= [0,3]
    return d

def pontos_por_time(jogos):
    '''lista lista > dict
    Recebe duas listas que representam 2 jogos jogados por exatamente 2 times. Em um jogo um time jogará em casa e no outro, jogará fora de casa, a ordem em que são escritos é o que define esse fator.
    Retorna os pontos acumulados nos 2 jogos pelos 2 times, levando em conta que uma vitória dá 3 pontos, um empate dá 1 ponto e uma derrota não dá pontos.
    Casos de teste: pontos_por_time([['fla','cor',[2,0]], ['cor','fla',[1,1]]]) == {'cor' : 1, 'fla': 4}
    pontos_por_time([['real','liv',[4,0]], ['liv','real',[1,3]]]) == {'liv' : 0, 'real' : 6} 
    pontos_por_time ([['river','boca',[2,2]], ['boca','river',[0,0]]]) == {'boca' : 2, 'river' : 2} '''
    t1 = jogos[0][0]
    t2 = jogos[0][1]
    gol1_t1 = jogos[0][2][0]
    gol2_t1 = jogos[0][2][1]
    gol1_t2 = jogos[1][2][0]
    gol2_t2 = jogos[1][2][1]
    ptsjogo1 = pts([gol1_t1, gol2_t1])
    ptsjogo2 = pts([gol1_t2, gol2_t2])
    ptstime1 = ptsjogo1[0] + ptsjogo2[1]
    ptstime2 = ptsjogo1[1] + ptsjogo2[0]
    
    return {t2 : ptstime2,
            t1 : ptstime1}