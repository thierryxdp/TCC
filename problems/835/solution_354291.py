def melhor_volta(matrizCorrida):
    
    menoresTempos = []
    menorTempo = 0
    volta = 0
    jogador = 0
    for linha in matrizCorrida:
		menoresTempos.append(min(linha))
        menorTempo = min(menoresTempos)
        volta = list.index(linha, menorTempo)
        jogador = list.index(menoresTempos, menorTempo)
    return (jogador + 1, menorTempo, volta + 1)