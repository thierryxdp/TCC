def pontos_por_time(lista):
    '''Função que recebe uma lista de dois elementos, onde cada elemento é tambem uma lista.
    A lista inteira tem informações do número de gols de dois jogos de futebol entre dois times
    (jogo de ida e jogo de volta), no seguinte formato: [[<nome do time1>,<nome do time2>,
    [<gols feito pelo time1>,<gols feito pelo time2>]],[<nome do time2>,<nome do time1>,
    [<gols feito pelo time2>,<gols feito pelo time1>]]. A saída é dada por um dicionario com o 
    nome dos times e as suas pontuações;
       list->dic'''
    tabela1={lista[0][0]:6,lista[1][0]:0}
    tabela2={lista[0][0]:4,lista[1][0]:1}
    tabela3={lista[0][0]:3,lista[1][0]:3}
    tabela4={lista[0][0]:4,lista[1][0]:1}
    tabela5={lista[0][0]:2,lista[1][0]:2}
    tabela6={lista[0][0]:1,lista[1][0]:4}
    tabela7={lista[0][0]:3,lista[1][0]:3}
    tabela8={lista[0][0]:1,lista[1][0]:4}
    tabela9={lista[0][0]:0,lista[1][0]:6}
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return tabela3
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
        return tabela2
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return tabela1
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return tabela6
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
        return tabela5
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return tabela4        
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return tabela9
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
        return tabela8
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return tabela7