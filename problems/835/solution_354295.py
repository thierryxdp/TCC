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
        jogador = list.index(menoresTempos, menorTempo)
        if menorTempo in linha:
            volta = list.index(linha, menorTempo)
        
    return (jogador + 1, menorTempo, volta + 1)