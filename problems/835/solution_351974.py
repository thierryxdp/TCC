def melhor_volta(m):
    """
    	Retorna de quem foi a melhor volta, com qual tempo e em que volta.
        list -> tuple
    """"
    tempo_voltas= []
    for i in range(6):
        list.append(tempo_voltas,min(m[i]))
    melhor_tempo=min(tempo_voltas)
    corredor=tempo_voltas.index(melhor_tempo)+1
    volta=m[corredor-1].index(melhor_tempo)+1
    return (corredor,melhor_tempo,volta)