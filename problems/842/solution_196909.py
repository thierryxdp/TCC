#Função que calcula a pontuação de um time após dois jogos entre si
#partida1,partida2
def pontos_por_time (partida1,partida2):
    """Função que retorna um dicionário com a pontuação de cada um dos dois times após 2 jogos"""
    """list;list->dic"""
    time0=partida1[0]
    time1=partida1[1]
    
    golspartida1time0=partida1[2][0]
    golspartida1time1=partida1[2][1]
    
    golspartida2time0=partida2[2][0]
    golspartida2time1=partida2[2][1]
    
    pontuacao0=0
    pontuacao1=0
    if golspartida1time0>golspartida1time1:
        pontuacao0+=3
    elif golspartida1time0<golspartida1time1:
        pontuacao1+=3
    else:
		pontuacao1+=1
        pontuacao0+=1
    if golspartida2time0>golspartida2time1:
        pontuacao0+=3
    elif golspartida2time0<golspartida2time1:
        pontuacao1+=3
    else:
		pontuacao1+=1
        pontuacao0+=1
    return {time0:pontuacao0,time1:pontuacao1}