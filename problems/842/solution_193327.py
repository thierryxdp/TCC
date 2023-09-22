def pontos_por_time(jogos):
    """Retorna um dicionário que indica o nome do time e o número total de pontos
    somados na fase, de acordo com os resultados dos jogos 1 e 2: list,list-> dict"""
    jogos == [['time1','time2',[gol1,gol2]],['time2','time1',[gol3,gol4]]]
    if jogos[0][2][0] > jogos[0][2][1] and jogos[1][2][0] < jogos[1][2][1]:
        return {time1 : 6 , time2 : 0}