def pontos_por_time(resultado):
    '''funcao que retorna a quantidade de pontos de um time em uma fase dados os resultados
    dos jogos de ida e volta
    entrada:
    lista(str do time mandante, str do visitante e outra lista com o resultado na mesma ordem)
    lista(str do time mandante, str do visitante e outra lista com o resultado na mesma ordem)'''
    pontos={}
    jogo_ida=resultado[0]
    jogo_volta=resultado[1]
    if jogo_ida[2][0]>jogo_ida[2][1] and jogo_volta[2][1]>jogo_volta[2][0]:
        pontos[jogo_ida[0]]=6
        pontos[jogo_ida[1]]=0
        return pontos
    if jogo_ida[2][1]>jogo_ida[2][0] and jogo_volta[2][0]>jogo_volta[2][1]:
        pontos[jogo_ida[0]]=6
        pontos[jogo_ida[1]]=0
        return pontos
    if jogo_ida[2][0]==jogo_ida[2][1] and jogo_volta[2][1]>jogo_volta[2][0]:
        pontos[jogo_ida[0]]=4
        pontos[jogo_ida[1]]=1
        return pontos
    if jogo_ida[2][0]>jogo_ida[2][1] and jogo_volta[2][1]==jogo_volta[2][0]:
        pontos[jogo_ida[0]]=4
        pontos[jogo_ida[1]]=1
        return pontos
    if jogo_ida[2][0]<jogo_ida[2][1] and jogo_volta[2][1]==jogo_volta[2][0]:
        pontos[jogo_ida[0]]=1
        pontos[jogo_ida[1]]=4
        return pontos
    if jogo_ida[2][0]==jogo_ida[2][1] and jogo_volta[2][1]<jogo_volta[2][0]:
        pontos[jogo_ida[0]]=1
        pontos[jogo_ida[1]]=4
        return pontos
    if jogo_ida[2][0]>jogo_ida[2][1] and jogo_volta[2][1]<jogo_volta[2][0]:
        pontos[jogo_ida[0]]=3
        pontos[jogo_ida[1]]=3
        return pontos
    if jogo_ida[2][0]<jogo_ida[2][1] and jogo_volta[2][1]>jogo_volta[2][0]:
        pontos[jogo_ida[0]]=3
        pontos[jogo_ida[1]]=3
        return pontos
    if jogo_ida[2][0]==jogo_ida[2][1] and jogo_volta[2][1]==jogo_volta[2][0]:
        pontos[jogo_ida[0]]=2
        pontos[jogo_ida[1]]=2
        return pontos