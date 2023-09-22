def melhor_volta(tempos):
    melhor_piloto = 0
    melhor_volta = 0
    melhor_tempo = float("inf")
    
    for (piloto, tempos_do_piloto) in enumerate(tempos):
        for (numero_da_volta, tempo) in enumerate(tempos_do_piloto):
            if tempo < melhor_tempo:
                melhor_piloto = piloto
                melhor_volta = numero_da_volta
                melhor_tempo = tempo
                
	return (melhor_piloto + 1, melhor_tempo, melhor_volta + 1)