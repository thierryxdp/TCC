def pontos_por_time(L):
    '''Função que recebe uma lista de dois elementos, onde cada elemento é tambem uma lista.
    A lista completa tem informações do número de gols de dois jogos de futebol entre dois times
    (jogo de ida e jogo de volta), no seguinte formato: [[<nome do time1>,<nome do time2>,
    [<gols feito pelo time1>,<gols feito pelo time2>]],[<nome do time2>,<nome do time1>,
    [<gols feito pelo time2>,<gols feito pelo time1>]]. A saída é dada por um dicionario com o 
    nome dos times e as suas pontuações;
       list->dic'''
    tabela1={L[0][0]:6,L[1][0]:0}
    tabela2={L[0][0]:4,L[1][0]:1}
    tabela3={L[0][0]:3,L[1][0]:3}
    tabela4={L[0][0]:4,L[1][0]:1}
    tabela5={L[0][0]:2,L[1][0]:2}
    tabela6={L[0][0]:1,L[1][0]:4}
    tabela7={L[0][0]:3,L[1][0]:3}
    tabela8={L[0][0]:1,L[1][0]:4}
    tabela9={L[0][0]:0,L[1][0]:6}
    if L[0][2][0]>L[0][2][1] and L[1][2][0]>L[1][2][1]:
        return tabela3
    if L[0][2][0]>L[0][2][1] and L[1][2][0]==L[1][2][1]:
        return tabela2
    if L[0][2][0]>L[0][2][1] and L[1][2][0]<L[1][2][1]:
        return tabela1
    if L[0][2][0]==L[0][2][1] and L[1][2][0]>L[1][2][1]:
        return tabela6
    if L[0][2][0]==L[0][2][1] and L[1][2][0]==L[1][2][1]:
        return tabela5
    if L[0][2][0]==L[0][2][1] and L[1][2][0]<L[1][2][1]:
        return tabela4        
    if L[0][2][0]<L[0][2][1] and L[1][2][0]>L[1][2][1]:
        return tabela9
    if L[0][2][0]<L[0][2][1] and L[1][2][0]==L[1][2][1]:
        return tabela8
    if L[0][2][0]<L[0][2][1] and L[1][2][0]<L[1][2][1]:
        return tabela7