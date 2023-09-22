def melhor_volta(tempo):
	""" Esta função busca a melhor volta de uma corrida  de kart 
	dict => tupla	"""
	melhor_volta  = list()

  	for linha in tempo:
    	menor_tempo = min(linha)  

    	melhor_volta.append(menor_tempo)

	return melhor_volta