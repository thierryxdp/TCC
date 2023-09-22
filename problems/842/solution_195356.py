def pontos_por_time(lista_fase):
    """dado uma lista, com duas outras listas dentro dela com 3 elementos em cada. A primeira lista indica
    o time A, o time B e o placar do jogo de ida deles. A segunda lista indica o time B, o time A e o placar
    do jogo de volta deles. Os placares também são escritos em formato de lista;
    list(list(str,str,list),list(str,str,list))->dict"""
    jogo1=lista_fase[0]
    jogo2=lista_fase[1]
    timeA=jogo1[0]
    timeB=jogo1[1]
    placarjogo1= jogo1[2]
    placarjogo2=jogo2[2]
    pontosTimeA=0
    pontosTimeB=0
    
    if placarjogo1[0]>placarjogo1[1]:
        pontosTimeA=pontosTimeA+3
    elif placarjogo1[0]==placarjogo1[1]:
        pontosTimeA=pontosTimeA+1
        pontosTimeB=pontosTimeB+1
    else:
        pontosTimeB=pontosTimeB+3
        
    if placarjogo2[0]>placarjogo2[1]:
        pontosTimeB=pontosTimeB+3
    elif placarjogo2[0]==placarjogo2[1]:
        pontosTimeA=pontosTimeA+1
        pontosTimeB=pontosTimeB+1
    else:
        pontosTimeA=pontosTimeA+3
    return {timeA:pontosTimeA,timeB:pontosTimeB}