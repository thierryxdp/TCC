def melhor_volta(tempos):
    melhor_piloto = 0
    melhor_volta = 0
    melhor_tempo = float("inf")
    
    for (tempos_do_piloto, piloto) in enumerate(tempos):
        for (tempo, numero_da_volta) in enumerate(tempos_do_piloto):
            if tempo < menor_tempo:
                melhor_piloto = piloto
                melhor_volta = numero_da_volta
                melhor_tempo = tempo
                
	return (piloto + 1, volta + 1, tempo)