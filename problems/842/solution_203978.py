def pontos_por_time(L):
    """ recebe uma lista de dois elementos , onde cada elemento é também uma lista.Sua função deve retornar um dicionário cujos os mapeamentos são: nome do time, numero total de pontos na fase, list -> dicionário"""
    jogoida=L[0]
    placarida=jogoida[2]
    time1=jogo_ida[0]
    time2=jogo_ida[1]
    jogovolta=L[1]
    placarvolta=jogovolta[2]
    
    if placarida[0]==placarida[1]:
        jogoidaA=1.1
    if placarida[0]>placarida[1]:
        jogoidaA=3.0
    if placarida[0]<placarida[1]:
        jogoidaA=0.3
    
    if placarvolta[0]==placarvolta[1]:
        jogovoltaB=1.1
    if placarvolta[0]>placarvolta[1]:
        jogovoltaB=3.0
    if placarvolta[0]<placarvolta[1]:
        jogovoltaB=0.3
    
    timeA=jogoidaA[0]+jogovoltaB[1]
    timeB=jogoidaA[1]+jogovoltaB[0]
    
    return{time1:timeA,time2:timeB}