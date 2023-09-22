def pontos_por_time(lista):
    """
	Função recebe uma lista de dois elementos, onde cada elemento é também uma lista.
    A lista tem informações do número de gols em dois jogos de futebol entre dois times(jogo da
    ida e jogo da volta) Ex: [[’Cormengo’, ’Flamínthians’, [1, 0]], 
    [’Flaminthians’, ’Cormengo’, [2, 2]]].
    Retorna um dicionário com as chaves referentes ao nome dos times e os valores referentes ao
    número de pontos que os times fizeram nos dois jogos. Vitoria=3 pontos, Empate=1 ponto,
    Derrota=0 pontos
    lista -> dicionario
    """
    jogo1=lista[0]
    jogo2=lista[1]
    placar1=jogo1[2]
    placar2=jogo2[2]
    time1=0
    time2=0
    if placar1[0]>placar1[1]:
        time1=3
    elif placar1[1]>placar1[0]:
        time2=3
    else:
        time1=1
        time2=1
    if placar2[0]>placar2[1]:
        time2=time2+3
    elif placar2[1]>placar2[0]:
        time1=time1+3
    else:
        time2=time2+1
        time1=time1+1
    if time1>time2:
        dicio={jogo1[0]:time1,jogo1[1]:time2}
    elif time1==time2:
        dicio={jogo1[0]:time1,jogo1[1]:time2}
    else:
        dicio={jogo1[1]:time2,jogo1[0]:time1}
    return dicio