def pontos_por_time(resultado):
    '''funcao que retorna a quantidade de pontos de um time em uma fase dados os resultados
    dos jogos de ida e volta
    entrada:
    lista(str do time mandante, str do visitante e outra lista com o resultado na mesma ordem)
    lista(str do time mandante, str do visitante e outra lista com o resultado na mesma ordem)'''
    pontos={}
    if resultado[0][2][0]>resultado[0][2][1] and resultado[1][2][1]>jogo_volta[1][2][0]:
        pontos[resultado[0][0]]=6
        pontos[resultado[0][1]]=0
        return pontos
    if resultado[0][2][1]>resultado[0][2][0] and resultado[1][2][0]>resultado[1][2][1]:
        pontos[resultado[0][0]]=0
        pontos[resultado[0][1]]=6
        return pontos
    if resultado[0][2][0]>resultado[0][2][1] and resultado[1][2][0]==resultado[1][2][1]:
        pontos[resultado[0][0]]=4
        pontos[resultado[0][1]]=1
        return pontos
    if resultado[0][2][1]>resultado[0][2][0] and resultado[1][2][0]==resultado[1][2][1]:
        pontos[resultado[0][0]]=4
        pontos[resultado[0][1]]=1
        return pontos
    if resultado[0][2][1]==resultado[0][2][0] and resultado[1][2][0]==resultado[1][2][1]:
        pontos[resultado[0][0]]=2
        pontos[resultado[0][1]]=2
        return pontos