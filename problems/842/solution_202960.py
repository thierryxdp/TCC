#Start your python function here
def pontos_por_time(jogo1[], jogo2[]):
	""" Retorna um dicionário com mapeamento: nome do time -> numero total de pontos na fase.
	entrada listas -> saida dicionário. """
	nome_t1 = jogo1[0][0]
    nome_t2 = jogo2[0][0]
    
    pontos_t1 = jogo1[2][0] + jogo2[2][1]
    pontos_t2 = jogo1[2][1] + jogo2[2][0]
    
    return {nome_t1:pontos_t1, nome_t2:pontos_t2}