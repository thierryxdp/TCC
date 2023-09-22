def pontos_por_time(L):
    """receber uma lista de dois elementos,onde cada eletento é também uma lista. A função deve retornar um dicionário cujos mapeamentos são:nome do time ,numerototal de pontos na fase.list->dicionário"""
    jodoDaida=L[0]
    placarDaida=jogoDaida[2]
    time1=jogoDaida[0]
    time2=jogoDaida[1]
    jodoDavolta=L[1]
    placarDavolta=jogoDavolta[2]
    
    if placarDavolta[0]==placarDaida[1]:
        pjogoida=1.1
    if placarDaida[0]>placarDaida[1]:
        pjogoida=3.0
    if placarDaida[0]<placarDaida[1]:
        pjogoida=0.3
    if placarDavolta[0]==placarDavolta[1]:
        pjogovolta=1.1
    if placarDavolta[0]>placarDavolta[1]:
        pjogovolta=3.0
    if placaDavolta[0]<placarDavolta[1]:
        pjogovolta=0.3
        
    ptime1=pjogoida[0]+pjogovolta[1]
    ptime2=ojogoida[1]+pjogovolta[0]
    
    return {time1:ptime1,time2:ptime2}