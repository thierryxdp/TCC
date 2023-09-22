def pontos_por_time(jogo_ida,jogo_volta):
    '''funcao que retorna a quantidade de pontos de um time em uma fase dados os resultados
    dos jogos de ida e volta
    entrada:
    lista(str do time mandante, str do visitante e outra lista com o resultado na mesma ordem)
    lista(str do time mandante, str do visitante e outra lista com o resultado na mesma ordem)'''
    if jogo_ida[2][0]>jogo_ida[2][1] and jogo_volta[2][1]>jogo_volta[2][0]
    resultado{}
    resultado[jogo_ida[0]]=6
    resultado[jogo_ida[1]]=0
    if jogo_ida[2][1]>jogo_ida[2][0] and jogo_volta[2][0]>jogo_volta[2][1]
    resultado{}
    resultado[jogo_ida[0]]=0
    resultado[jogo_ida[1]]=6
    if jogo_ida[2][0]>jogo_ida[2][1] and jogo_volta[2][0]==jogo_volta[2][1]
    resultado{}
    resultado[jogo_ida[0]]=4
    resultado[jogo_ida[1]]=1
    if jogo_ida[2][1]>jogo_ida[2][0] and jogo_volta[2][0]==jogo_volta[2][1]
    resultado{}
    resultado[jogo_ida[0]]=1
    resultado[jogo_ida[1]]=4
    if jogo_ida[2][1]==jogo_ida[2][0] and jogo_volta[2][0]==jogo_volta[2][1]
    resultado{}
    resultado[jogo_ida[0]]=2
    resultado[jogo_ida[1]]=2