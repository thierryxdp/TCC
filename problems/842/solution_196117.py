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
    ###dicio={"Cormengo":0,"Flamínthians":0} ###talvez alterar aqui
    ###para o dicionario ser criado dependendo do nome do time
    jogo1=lista[0]
    jogo2=lista[1]
    dicio={jogo1[0]:0,jogo1[1]:0}
    placar1=jogo1[2]
    placar2=jogo2[2]
    if placar1[0]>placar1[1]:
        dicio[jogo1[0]]=3
    elif placar1[1]>placar1[0]:
        dicio[jogo1[1]]=3
    else:
        dicio[jogo1[0]]=1
        dicio[jogo1[1]]=1
    if placar2[0]>placar2[1]:
        dicio[jogo1[1]]=3+dicio[jogo1[1]]
    elif placar2[1]>placar2[0]:
        dicio[jogo1[0]]=3+dicio[jogo1[0]]
    else:
        dicio[jogo1[0]]=1+dicio[jogo1[0]]
        dicio[jogo1[1]]=1+dicio[jogo1[1]]
    return dicio