def pontos_por_time(jogos):
    jogos=[jogo_ida,jogo_volta]
    jogo_ida=[time1,time2,[gol1ida,gol2ida]]
    jogo_volta=[time2,time1,[gol2volta,gol1volta]]
    if gol1ida-gol2ida>0:
        r1ida=3 
        r2ida=0
    if gol1ida-gol2ida<0:
        r1ida=0 
        r2ida=3
    if gol1ida==gol2ida:
        r1ida=1=r2ida
    if gol1volta-gol2volta>0:
        r1volta=3 
        r2volta=0
    if gol1volta-gol2volta<0:
        r1volta=0 
        r2volta=3
    if golvolta==gol2volta:
        r1volta=1=r2volta    
    r1=r1ida+r1volta
    r2=r2ida+r2volta
    resultado_fase={time1:r1,time2:r2}
    return reultado_fase