def pontos_por_time (L1):
    '''
       Função que recebe uma lista (L1) de dois elementos,
       onde cada elemento é tambem uma lista com informações
       do numero de gols em dois jogos de fultebol entre
       dois times no seguinte formato [['cormengo', 
       'flaminthians', [1,0]],['flaminthians','cormengo',
       [2,2]]], e retorna um dicionario com o nome do time 
       associado ao total de pontos na fase. Os pontos por
       fase são a soma dos pontos ganhos por cada vitoria
       ou empate nos jogos (3 pontos a vitoria e 1 o 
       empate);
       list -> dict
    '''
    #L1 = [L1[0], L1[2]]
    #L1[0] = ['time1','time2',[p1,p2]]
    time1 = L1[0][0]
    p1 = L1[0][2][0]
    time2 = L1[0][1]
    p2 = L1[0][2][1]
    #L1[1] = ['time01','time02',[p01,p02]]
    time01 = L1[1][0]
    p01 = L1[1][2][0]
    time02 = L1[1][1]
    p02 = L1[1][2][1]
    if p1>p2 and p01>p02:
        return {str(time1):'6', str(time2):'0'}
    else:
        return 'sla'
    #dic {'L1[1][0]':'', 'L1[1][1]':'gol'}