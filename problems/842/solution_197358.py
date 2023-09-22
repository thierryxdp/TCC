def pontos_por_time(jogos):
    """
    	Função que dá o total de pontos de uma fase entre 
        dois times.
        list(list,list) -> dict
    """
    nota1 = 0
    nota2 = 0
    jogo1 = jogos[0]
    time1 = jogo1[0]
    time2 = jogo1[1]
    pontos1 = jogo1[2]
    jogo2 = jogos[1]
    pontos2 = jogo2[2]
    
    if pontos1[0]==pontos1[1]:
        nota1 = nota1 + 1
    if pontos2[0]==pontos2[1]:
        nota2 = nota2 + 1
    fase = dict(zip([time1,time2],[nota1,nota2]))
    return fase