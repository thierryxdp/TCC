def pontos_por_time(lista):
    '''retorna a pontuação de cada time na fase
       list-->dicionario'''
    jogo1=lista[0]
    jogo2=lista[1]
    time1=jogo1[0]
    time2=jogo1[1]
    placar1=jogo1[2]
    placar2=jogo2[2]
    #jogo1
    if placar1[0]==placar1[1]:
        pts1=1
        pts2=1
    elif placar1[0]>placar1[1]:
        pts1=3
        pts2=0
    else:
        pts1=0
        pts2=3
    time1=jogo2[1]
    time2=jogo2[0]
    #jogo2
    if placar2[0]==placar2[1]:
        pts1=pts1+1
        pts2=1+pts2
    elif placar2[0]>placar2[1]:
        pts1=3+pts1
    else:
        pts2=3+pts2
    return {time1:pts1,time2:pts2}