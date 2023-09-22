def pontos_por_time(jogo1,jogo2=None):
	""" Retorna o total de pontos de um time em uma fase, dado duas listas.
	    entrada: lista -> saida: dicionário. """
    
	pontuacao_time1 = jogo1[2][0] + jogo2[2][1]
	pontuacao_time2 = jogo1[2][1] + jogo2[2][0]
    
	return {jogo1[0]:pontuacao_time1, jogo2[0]: pontuacao_time2}