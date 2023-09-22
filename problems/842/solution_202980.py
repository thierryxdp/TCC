#Start your python function here
def pontos_por_time(jogo1, jogo2):
	""" Retorna o total de pontos de um time em uma fase, dado duas listas.
    entrada: lista -> saida: dicionário. """
    
    pontos_time1 = jogo1[2][0] + jogo2[2][1]
    return pontos_time1