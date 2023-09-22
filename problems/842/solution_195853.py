def pontos_por_time(s):
    jogo1=s[0]
    jogo2=s[1]
    res={}
    time1=jogo2[0]
    time2=jogo2[1]
    gol11=jogo1[2][0]
    gol21=jogo1[2][1]
    gol12=jogo2[2][0]
    gol22=jogo2[2][1]
    if gol11==gol21:
        res[time1]=1
        res[time2]=1
    if gol11>gol21:
        res[time1]=3
        res[time2]=0
    if gol21>gol11:
        res[time1]=0
        res[time2]=3
        
    if gol12==gol22:
        res[time1]=res[time1]+1
        res[time2]=res[time2]+1
    if gol12>gol22:
        res[time1]=res[time1]+3
    if gol22>gol12:
        res[time2]=res[time2]+3
    return res