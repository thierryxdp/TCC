pontos_por_time(lista):
    """Função que, dada uma lista que contém informações a respeito do número de gols em dois jogos de futebol entre dois times, retorna um dicionário que tem como chaves os nomes dos times e, como valor, o número total de pontos de cada time; lista->dicionário"""
    jogo1 = lista[0]
    jogo1[0] = time1
    
    jogo2 = lista[1]
    jogo2[0] = time2
    
    placar1 = jogo1[2]
    gols_time1_jogo1 = placar1[0]
    gols_time2_jogo1 = placar1[1]
    
    placar2 = jogo2[2]
    gols_time2_jogo2 = placar2[0]
    gols_time1_jogo2 = placar2[1]
    
    dicionario = {time1:pontos1,time2:pontos1}
    
    if(gols_time1_jogo1 == gols_time2_jogo1 and gols_time2_jogo2 == gols_time1_jogo2):
        pontos1 = 2
        pontos2 = 2
        return dicionario
    elif(gols_time1_jogo1 > gols_time2_jogo1 and gols_time2_jogo2 > gols_time1_jogo2):
        pontos1 = 3
        pontos2 = 3
        return dicionario
    elif(gols_time1_jogo1 < gols_time2_jogo1 and gols_time2_jogo2 < gols_time1_jogo2):
        pontos1 = 3
        pontos2 = 3
        return dicionario
    elif(gols_time1_jogo1 > gols_time2_jogo1 and gols_time2_jogo2 < gols_time1_jogo2):
        pontos1 = 6
        pontos2 = 0
        return dicionario
    elif(gols_time1_jogo1 < gols_time2_jogo1 and gols_time2_jogo2 > gols_time1_jogo2):
        pontos1 = 0
        pontos2 = 6
        return dicionario
    elif(gols_time1_jogo1 == gols_time2_jogo1 and gols_time2_jogo2 < gols_time1_jogo2):
        pontos1 = 4
        pontos2 = 1
        return dicionario
    elif(gols_time1_jogo1 == gols_time2_jogo1 and gols_time2_jogo2 > gols_time1_jogo2):
        pontos1 = 1
        pontos2 = 4
        return dicionario
    elif(gols_time1_jogo1 > gols_time2_jogo1 and gols_time2_jogo2 == gols_time1_jogo2):
        pontos1 = 4
        pontos2 = 1
        return dicionario
    elif(gols_time1_jogo1 < gols_time2_jogo1 and gols_time2_jogo2 == gols_time1_jogo2):
        pontos1 = 1
        pontos2 = 4
        return dicionario