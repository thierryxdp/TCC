def pontos_por_time(lista=[]):
    '''Faça uma função que receba uma lista de dois elementos, onde cada elemento é também uma lista, lista -> dicionário'''
    jogo_ida=lista[0]
    jogo_volta=lista[1]
    time1=jogo_ida[0]
    time2=jogo_ida[1]
    placar_ida=jogo_ida[2]
    placar_volta=jogo_volta[2]
    if (placar_ida[0])>(placar_ida[1]) and (placar_volta[1])>(placar_volta[0]):
        return {jogo_ida[0]: 6, jogo_ida[1]: 0}
    elif (placar_ida[0])<(placar_ida[1]) and (placar_volta[1])<(placar_volta[0]):
        return {jogo_ida[0]: 0, jogo_ida[1]: 6}
    elif ((placar_ida[0])<(placar_ida[1]) and (placar_volta[1])>(placar_volta[0])) or ((placar_ida[0])>(placar_ida[1]) and (placar_volta[1])<(placar_volta[0])): 
        return {jogo_ida[0]: 3, jogo_ida[1]: 3}
    elif (placar_ida[0])>(placar_ida[1]) and (placar_volta[1])<(placar_volta[0]):
        return {jogo_ida[0]: 3, jogo_ida[1]: 3}
    elif (placar_ida[0])<(placar_ida[1]) and (placar_volta[1])==(placar_volta[0]):
        return {jogo_ida[0]: 1, jogo_ida[1]: 4}
    elif (placar_ida[0])==(placar_ida[1]) and (placar_volta[1])<(placar_volta[0]):
        return {jogo_ida[0]: 1, jogo_ida[1]: 4}
    else:
        if((placar_ida[0])==(placar_ida[1]) and (placar_volta[1])==(placar_volta[0])): 
            return {jogo_ida[0]: 2, jogo_ida[1]: 2}