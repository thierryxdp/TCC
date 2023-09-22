def pontos_por_time(lista):
    """função que recebe uma lista de dois elementos,
    onde cada elemento também é uma lista, que contém
    o número de gols em dois jogos de futebol entre dois times
    no seguinte formato de exemplo:
    [['Cormengo','Flamínthians',[1,0]], #jogo de ida
    ['Flamínthians','Cormengo',[2,2]]] #jogo de volta
    e retorna um dicionário cujos mapeamentos são o nome
    do time e quantidade de pontos na fase.
    lista, lista -> dicionário"""
    L=lista
    ida=L[0]
    volta=L[1]
    pontos_ida=ida[2]
    pontos_volta=volta[2]
    time1=ida[0]
    time2=ida[1]
    #pontos_ida[0] -> time1, pontos_ida[1] -> time2
    #pontos_volta[0] -> time2, pontos_volta[1] -> time1
    i0=pontos_ida[0]
    i1=pontos_ida[1]
    v0=pontos_volta[0]
    v1=pontos_volta[1]
    tupla_placar_time1=()
    tupla_placar_time2=()
    
    #jogo de ida
    if(i0>i1):#vitótia time 1
        tupla_placar_time1=tupla_placar_time1+(3,)
        tupla_placar_time2=tupla_placar_time2+(0,)
    elif(i0==i1):#empate
        tupla_placar_time1=tupla_placar_time1+(1,)
        tupla_placar_time2=tupla_placar_time2+(1,)
    else: #vitória time 2
        tupla_placar_time2=tupla_placar_time2+(3,)
        tupla_placar_time1=tupla_placar_time1+(0,)
    
    #jogo de volta
    if(v0>v1):#vitória time 2
        tupla_placar_time2=tupla_placar_time2+(3,)
        tupla_placar_time1=tupla_placar_time1+(0,)
    elif(v0==v1):#empate
        tupla_placar_time1=tupla_placar_time1+(1,)
        tupla_placar_time2=tupla_placar_time2+(1,)
    else:#vitória time 1
        tupla_placar_time1=tupla_placar_time1+(3,)
        tupla_placar_time2=tupla_placar_time2+(0,)
         
    #contagem dos pontos
    
    #time 1
    placar_ponots_time1=()
    placar_pontos_time1=tupla_placar_time1[0]+tupla_placar_time1[1]+tupla_placar_time1[2]
    
    #time 2
    placar_pontos_time2=()
    placar_pontos_time2=tupla_placar_time2[0]+tupla_placar_time2[1]+tupla_placar_time2[2]

    placar={str(time1):placar_pontos_time1, str(time2):placar_pontos_time2}
    
    return placar