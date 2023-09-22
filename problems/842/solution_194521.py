def pontos_por_time(lista):
    """Função que recebe uma lista composta por duas listas, ambas com dois times e seus gols no primeiro e segundo jogos respectivamente e retorna um dicionário com o nome do time e sua pontuação total na partida.
    list -> dicionário
    Explicação: a função analisa as possibilidades diferentes, os dois times empatarem nos dois jogos, empatarem na primeira e terem saldos diferentes no segundo e saldos diferentes no primeiro e empate no segundo, retornando 3 pontos para vitórias, 1 para empates e nenhum para derrotas, somando a pontuação do primeiro e segundo jogo de cada um para calcular seu saldo final da partida."""   
    [time1,time2,[gol11,gol21]]=lista[0]
    [time2,time1,[gol22,gol12]]=lista[1]
    if gol11==gol21:
        if gol22==gol12:
            return {time2:2,time1:2}
        elif gol22>gol12:
            return {time2:1,time1:4}
        elif gol12>gol22:
            return {time1:4,time2:1}
    if gol11>gol21:
        if gol22==gol12:
            return {time2:1,time1:4}
        elif gol22>gol12:
            return {time2:3,time1:3}
        elif gol12>gol22:
            return {time2:0,time1:6}
    if gol21>gol11:
        if gol22==gol12:
            return {time2:4,time1:1}
        elif gol22>gol12:
            return {time2:6,time1:0}
        elif gol12>gol22:
            return {time2:3,time1:3}