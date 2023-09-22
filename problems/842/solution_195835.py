def pontos_por_time(jogo):
    jogo1=jogo[0]
    jogo2=jogo[1]
    time1=jogo1[0]
    time2=jogo1[1]
    placar1=jogo1[2]
    x=placar1[0]
    y=placar1[1]
    time23=jogo2[0]
    time13=jogo2[1]
    placar2=jogo2[2]
    t=placar2[0]
    r=placar2[1]
    
    
    if x==y:
       a=1
       s=1
    if x>y:
        a=3
        s=0
    if x<y:
        a=0
        s=3
    if t==r:
        z=1
        c=1
    if t>r:
        z=3
        c=0
    if t<r:
        z=0
        c=3
        
    pontuacao = { time1:a+c ,time2:s+z}
    return pontuacao