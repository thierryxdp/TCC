def melhor_volta(matrizCorrida):
    """
    	Recebe uma matriz com dados sobre corredores,
        suas voltas e tempos.
        Retornar os dados da melhor volta.
        list --> tuple
    """
    menoresTempos = []
    menorTempo = 0
    volta = 0
    jogador = 0
    for linha in matrizCorrida:
		menoresTempos.append(min(linha))
        menorTempo = min(menoresTempos)
        volta = list.index(menoresTempos, menorTempo)
        jogador = list.index(menoresTempos, menorTempo)
    return (jogador + 1, menorTempo, volta)