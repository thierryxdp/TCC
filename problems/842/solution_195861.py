def pontos_por_time(s):
    jogo1=s[0]
    jogo2=s[1]
    res={}
    time2=jogo2[0]
    time1=jogo2[1]
    gol1=jogo1[2]
    gol2=jogo2[2]
    gol11=gol1[0]
    gol21=gol1[1]
    gol12=gol2[0]
    gol22=gol2[1]
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
        res[time2]=res[time2]+1
        res[time1]=res[time1]+1
    if gol12>gol22:
        res[time2]=res[time2]+3
        res[time1]=res[time1]+0
    if gol22>gol12:
        res[time1]=res[time1]+3
        res[time2]=res[time2]+0
    return res