def pontos_por_time(lista):
    '''funcao que dado os nomes de dois times e os numeros de gols,retorna os nomes dos times com seus respectivos pontos; lista -> dicionario'''
    [[time1,time2,[gols1_,gols2_]],[time2,time1.[gols2,gols1]]] = lista
    resultado_jogo = {}
    if (gols1_ > gols2_) and (gols1 > gols2):
        resultado_jogo = {time1:6,time2:0}
    elif (gols1_ < gols2_) and (gols1 < gols2):
        resultado_jogo = {time1:0,time2:6}
    elif (gols1_ > gols2_) and (gols1 < gols2):
        resultado_jogo = {time1:3,time2:3}
    elif (gols1_ < gols2_) and (gols1 > gols2):
        resultado_jogo = {time1:3,time2:3}
    elif (gols1_ == gols2_) and (gols1 == gols2):
        resultado_jogo = {time1:2,time2:2}
    elif (gols1_ == gols2_) and (gols1 > gols2):
        resultado_jogo = {time1:4,time2:1}
    elif (gols1_ == gols2_) and (gols1 < gols2):
        resultado_jogo = {time1:1,time2:4}
    elif (gols1_ > gols2_) and (gols1 == gols2):
        resultado_jogo = {time1:4,time2:1}
    elif (gols1_ < gols2_) and (gols1 == gols):
        resultado_jogo = {time1:1,time2:4}
    return resultado_jogo