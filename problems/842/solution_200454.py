def pontos_por_time(lista):
    ''''''
    jogo1=lista[0]
    jogo2=lista[1]
    time1=lista[0][0]
    time2=lista[0][1]
    pontostime1=0
    pontostime2=0
    placar1=lista[0][2]
    placar2=lista[1][2]
    if placar1[0]>placar1[1]:
        pontostime1=pontostime1+3
    elif placar1[0]<placar1[1]:
        pontostime2=pontostime2+3
    elif placar1[0]==placar1[1]:
        pontostime1=pontostime1+1
        pontostime2=pontostime2+1
    if placar2[0]>placar2[1]:
        pontostime1=pontostime1+3
    elif placar2[0]<placar2[1]:
        pontostime2=pontostime2+3
    elif placar2[0]==placar2[1]:
        pontostime1=pontostime1+1
        pontostime2=pontostime2+1
    return {time1:pontostime1,time2:pontostime2}