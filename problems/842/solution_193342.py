def soma(x,y):
    """Retorna a soma dosa termos dados como entrada"""
    return x+y

def pontos_por_time(jogos):
    """Retorna um dicionário que indica o nome do time e o número total de pontos
    somados na fase, de acordo com os resultados dos jogos 1 e 2: list,list-> dict"""
    [[time1,time2,[gol1,gol2]],[time2,time1,[gol3,gol4]]] = jogos
    if gol1 > gol2 and gol4>gol3
        ptime1 = 6
        ptime2 = 0
    elif gol1 == gol2:
        ptime1 = 1
        ptime2 = 1
    elif gol1< gol2:
        ptime1 = 0
        ptime2 = 3
        
        return {time1:ptime1, time2:ptime2}