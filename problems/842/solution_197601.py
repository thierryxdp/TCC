def pontos_por_time(lista1):
    time1jogo2=lista1[1][2][1]
    time1jogo1=lista1[0][2][0]
    time2jogo2=lista1[1][2][0]
    time2jogo1=lista1[0][2][1]
    pontostime1=0
    pontostime2=0
    if time1jogo2>time2jogo2:
        pontostime1=(pontostime1+3)
    if time1jogo2<time2jogo2:
        pontostime2=(pontostime1+3)
    if time1jogo2==time2jogo2:
        pontostime1=(pontostime1+1)
        pontostime2=(pontostime2+1)
    if time1jogo1>time2jogo1:
        pontostime1=(pontostime1+3)
    if time1jogo1<time2jogo1:
        pontostime2=(pontostime2+3)
    if time1jogo1==time2jogo1:
        pontostime1=(pontostime1+1)
        pontostime2=(pontostime2+1)
    if pontostime2>pontostime1:
        return {lista1[0][1]:pontostime2,lista1[0][0]:pontostime1}
    elif pontostime1>pontostime2:
        return {lista1[0][1]:pontostime1,lista1[0][0]:pontostime2}
    else: 
        return {lista1[0][1]:pontostime1,lista1[0][0]:pontostime2}