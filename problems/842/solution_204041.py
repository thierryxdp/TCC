def pontos_por_time(lista):
    """função que recebe UMA lista de dois elementos,onde cada elemento é também uma lista.A função deve retornar um dicionário, cujos os mapeamentos são:nome do time,numero total de pontosna fase ,list->dicionario"""
    jogoDaida=lista[0]
    placarDaida=jogoDaida[2]
    time01=jogoDaida[1]
    time02=jogoDaida[1]
    jogoDavolta=lista[1]
    placarDavolta=jogoDavolta[2]
    
    if placarDaida[0]==placarDaida[1]:
        jogoidaA=1,1
    if placarDaida[0]>placarDaida[1]:
        jogoidaA=3,0
    if placarDaida[0]<placarDaida[1]:
        jogoidaA=0,3
    if placarDavolta[0]==placarDavolta[1]:
        jogovoldaB=1,1
    if placarDavolta[0]>placarDavolta[1]:
        jogovoldaB=3,0
    if placarDavolta[0]<placarDavolta[1]:
        jogovoldaB=0,3
        
        timeA=jogoidaA[0]+jogovoldaB[1]
        timeB=jogoidaA[1]+jogovoldaB[0]
    return {time01:timeA,time02:timeB}