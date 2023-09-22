def pontos_por_time(jogo):
    ''''''
    
    jogoi = [t1,t2,[0,1]]
    jogov = [t2,t1,[0,1]]
    
    jogo = [jogoi, jogov]
    t1 = jogoi[0]
    t2 = jogov[0]
    pontos_t1 = jogoi[2][0] + jogov[2][1]
    pontos_t2 = jogoi[2][1] + jogov[2][0]
    
    return {t1:pontos_t1, t2:pontos_t2}