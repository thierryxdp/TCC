def pontos_por_time(lista):
    '''função que recebe uma lista de dois elementos que também são uma lista
    	em que a lista completa tem os nomes de dois times e número de gols
        nas partidas de ida e volta, e retorna um dicionário com a quantidade 
        de pontos referentes a cada time naquela fase
        list -> dic
    '''
    jogodeida = lista[0]
    jogodevolta = lista[1]
    timeAida = str(jogodeida[0])
    timeBida = str(jogodeida[1])
    timeAvolta = jogodevolta[1]
    timeBvolta = jogodevolta[0]
    golspartidaida = jogodeida[2]
    golspartidavolta = jogodevolta[2]
    golstimeAida = golspartidaida[0]
    golstimeBida = golspartidaida[1]
    golstimeAvolta = golspartidavolta[1]
    golstimeBvolta = golspartidavolta[0]
    if golstimeAida > golstimeBida:
        pontosAida = 3
        pontosBida = 0
    if golstimeAida == golstimeBida:
        pontosAida = 1
        pontosBida = 1
    if golstimeAida < golstimeBida:
        pontosAida = 0
        pontosBida = 3
    if golstimeAvolta > golstimeBvolta:
        pontosAvolta = 3
        pontosBvolta = 0
    if golstimeAvolta == golstimeBvolta:
        pontosAvolta = 1
        pontosBvolta = 1
    if golstimeAvolta < golstimeBvolta:
        pontosAvolta = 0
        pontosBvolta = 3
    pontostime = {timeAida: pontosAida+pontosAvolta , timeBida: pontosBida+pontosBvolta}
    return pontostime