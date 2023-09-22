def pontos_por_time(lista):
    """ recebe uma lista de dois elementos , onde cada elemento é também uma lista.Sua função deve retornar um dicionário cujos os mapeamentos são: nome do time, numero total de pontos na fase, list -> dicionário"""
    jogo_volta=lista[1]
    placar_volta=jogo _volta[2]
    time01=jogo_ida[0]
    time02=jogo_ida[1]
    jogo_ida=lista[0]
    placar_ida=jogo_ida[2]
    
    if placar_ida[0]==placar_ida[1]:
        jogoidaA=1.1
    if placar_ida[0]<placar_ida[1]:
        jogoidaA=3.0
    if placar_ida[0]<placar_ida[1]:
        jogoidaA=0.3
    if placar_volta[0]==placar_volta[1]:
        jogovoltaB=1.1
    if placar_volta[0]>placar_volta[1]:
        jogovoltaB=3.0
    if placar_volta[0]<placar_volta[1]:
        jogovoltaB=0.3
    
    timeA=jogoidaA[0]+jogovoltaB[1]
    timeB=jogoidaA[1]+jogovoltaB[0]
    return{time01:timeA,time02:timeB}