def pontos_por_time(tabela):
    """Recebe uma lista com os resultados de dois jogos entre
	duas equipes, e retorna um dicionário com os pontos calculados;
	lista --> dict"""
    Jogo1 = tabela[0]
    Jogo2 = tabela[1]
    partida1 = Jogo1[2]
    partida2 = Jogo2[2]
    if partida1[0] > partida1[1] and partida2[0] > partida2[1]:
        return {Jogo1[0]:3, Jogo2[0]:3}
    elif partida1[0] > partida1[1] and partida2[0] < partida2[1]:
        return {Jogo1[0]:6, Jogo2[0]:0}
    elif partida1[0] < partida1[1] and partida2[0] > partida2[1]:
        return {Jogo1[0]:0, Jogo2[0]:6}
    elif partida1[0] == partida1[1] and partida2[0] == partida2[1]:
        return {Jogo1[0]:2, Jogo2[0]:2}
    elif partida1[0] > placar_ida[1] and placar_volta[0] == placar_volta[1]:
        return {ida[0]:4, Jogo2[0]:1}
    elif partida1[0] == partida1[1] and placar_volta[0] < placar_volta[1]:
        return {Jogo1[0]:4, Jogo2[0]:1}
    else:
        return {ida[0]:3, Jogo2[0]:3}