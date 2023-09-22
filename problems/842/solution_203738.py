def pontos_por_time(L):
    """recebe uma lista de 2 elementos,onde cada elemento tambem e uma
    lista. retorna um dicionario cujos mapeamento sao:nome de um time->numero
    de pontos. list->dicionario"""
    
    jogoIda=L[0]
    placarIda=jogoIda[2]
    time1=jogoIda[0]
    time2=jogoIda[1]
    jogoVolta=L[1]
    placarVolta=jogoVolta[2]
    
    if placarIda[0]==placarIda[1]:
       pjogoida=1,1
    if placarIda[0]>placarIda[1]:
       pjogoida=3,0
    if placarIda[0]<placarIda[1]:
       pjogoida=0,3
    
    if placarVolta[0]==placarVolta[1]:
       pjogovolta=1,1
    if placarVolta[0]>placarVolta[1]:
       pjogovolta=3,0
    if placarVolta[0]<placarVolta[1]:
       pjogovolta=0,3
    
    ptime1= pjogoida[0]+pjogovolta[1]
    ptime2= pjogoida[1]+pjogovolta[0]
    
    return {time1:ptime1, time2:ptime2}