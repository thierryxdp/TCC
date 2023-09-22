def pontos_por_time (lista):
    '''função em que dada uma lista de dois elementos onde cada elemento também
    é uma lista. A lista completa tem informações do número de gols em dois
    jogos de futebol entre dois times (jogo de ida e jogo de volta), no seguinte
    formato: [[<nomedotime1>,<nomedotime2>,[<golsdotime1>,<golsdotime2>]],
    [<nomedotime2>,<nomedotime1>,[<golsdotime2>,<golsdotime1>]]]. A saída é dada
    por um dicionário com os nomes dos times e suas pontuações;
    list -> dict'''
    tabela1={lista[0][0]:6,lista[1][0]:0}
    tabela2={lista[0][0]:3,lista[1][0]:3}
    tabela3={lista[0][0]:0,lista[1][0]:6}
    tabela4={lista[0][0]:4,lista[1][0]:1}
    tabela5={lista[0][0]:1,lista[1][0]:4}
    tabela6={lista[0][0]:2,lista[1][0]:2}
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
    #quando o time 1 ganhar os dois jogos
        return tabela1
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
    #quando o time 1 ganhar o primeiro e o time 2 ganhar o segundo
        return tabela2
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
    #quando o time 1 ganhar o segundo e o time 2 ganhar o primeiro
        return tabela2
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
    #quando o time 2 ganhar os dois jogos
        return tabela3
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
    #quando o time 1 ganhar o primeiro jogo e os dois empatarem o segundo
        return tabela4
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
    #quando o time 1 ganhar o segundo jogo e os dois empatarem o primeiro
        return tabela4
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
    #quando o time 2 ganhar o primeiro jogo e os dois empatarem o segundo
        return tabela5
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
    #quando o time 2 ganhar o segundo jogo e os dois empatarem o primeiro
        return tabela5
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
    #quando os dois times empatarem os dois jogos
        return tabela6