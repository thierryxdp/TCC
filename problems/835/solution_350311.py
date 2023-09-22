def melhor_volta(matriz):
    """
    	dada uma matriz 6x10, indica quem foi o melhor corredor, seu melhor tempo, e sua melhor volta
    	list -> tuple
    """
    menores_tempos = []
    for i in range(len(matriz)):
        menores_tempos.append(min(matriz[i]))
    melhor_tempo=min(menores_tempos)
    melhor_corredor=menores_tempos.index(menor_tempo)
    melhor_volta=matriz[melhor_corredor].index(menor_tempo)
    return (melhor_corredor+1,menor_tempo,melhor_volta+1)