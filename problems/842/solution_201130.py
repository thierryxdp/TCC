def pontos_por_time(jogo_ida,placar1,jogo_volta,placar2):
    '''função que, dados placares dos dois jogos, retorna um dicionário com a pontuação de cada time
       list -> dict'''
    if placar1[0]>placar1[1]:
     x1=3
     x2=0
    if placar1[0]==placar1[1]:
     x1=1
     x2=1
    if placar1[0]<placar1[1]:
     x1=0
     x2=3
    if placar2[0]>placar2[1]:
     y1=3+x2
     y2=0+x1
    if placar2[0]==placar2[1]:
    y1=1+x2
    y2=1+x1
    if placar2[0]<placar2[1]:
    y1=0+x2
    y2=3+x1
    return {jogo_ida[0]:y2,jogo_ida[1]:y1}