def pontos_por_time (placares):
    """Função que retorna um dicionário com a pontuação de cada um dos dois times após 2 jogos"""
    """list->dic"""
    time1=placares[0][0]
    time2=placares[0][1]
    
    golspartida1time1=placares[0][2][0]
    golspartida1time2=placares[0][2][1]
    
    golspartida2time1=placares[1][2][1]
    golspartida2time2=placares[1][2][0]
    
    pontuacaotime1=0
    pontuacaotime2=0
    
    if golspartida1time1>golspartida1time2:
        pontuacaotime1+=3
    elif golspartida1time1<golspartida1time2:
        pontuacaotime2+=3
    else:
		pontuacaotime1+=1
		pontuacaotime2+=1
    if golspartida2time1>golspartida2time2:
        pontuacaotime1+=3
    elif golspartida2time1<golspartida2time2:
        pontuacaotime2+=3
    else:
		pontuacaotime1+=1
        pontuacaotime2+=1
    return {time1:pontuacaotime1,time2:pontuacaotime2}