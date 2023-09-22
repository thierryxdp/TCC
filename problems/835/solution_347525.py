def melhor_volta(matriz):
    """jgjg"""
    melhorTempo = (0,0,0)
    nJogador = 0
    for jogador in matriz:
        melhorTempoJogador = min(jogador)
        if melhorTempoJogador<melhorTempo[1]:
            melhorTempo = (nJogador+1, melhorTempoJogador, jogador.index(melhorTempoJogador)+1)
        nJogador+=1
    return melhorTempo