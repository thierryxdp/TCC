def pontos_jogo (time1, time2):
    """função, que dado dois valores de gols, retorna a pontuação do primeiro
    int,int->int"""
    tamanho1=range (time1)
    tamanho2=range (time2)
    if (time1>time2):
        return 3
    elif(time1==time2):
        return 1
    else:
        return 0
        
def pontos_por_time (j):
    """função, que dada duas listas(cada um composto por listas tambem),
    retorna um dicionario contendo o nome dos times atrelado ao numero de pontos que
    o mesmo fez na fase
    list,list->dict"""
#    pontos do time 1
    pontos_T1=pontos_jogo(j[0][2][0],j[0][2][1])+pontos_jogo(j[1][2][1],j[1][2][0])
#    pontos do time 2
    pontos_T2=pontos_jogo(j[0][2][1],j[0][2][0])+pontos_jogo(j[1][2][0],[1][2][1])

    return {j1[0][0]:pontos_T1,j1[0][1]:pontos_T2}