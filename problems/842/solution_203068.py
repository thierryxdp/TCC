#Start your python function here
def pontos_por_time(jogo1):
	""" Retorna o total de pontos de um time em uma fase, dado duas listas.
    entrada: lista -> saida: dicionário. """
    pontuacao_time1 = 0
    pontuacao_time2 = 0
   
    if (jogo1[0][2][0] > jogo1[0][2][1]):
        pontuacao_time1 = pontuacao_time1 + 3
       
    elif(jogo1[0][2][0] == jogo1[0][2][1]):
        pontuacao_time1 = pontuacao_time1 + 1
        pontuacao_time2 = pontuacao_time2 + 1
       
    elif(jogo1[0][2][0] < jogo1[0][2][1]):
    	pontuacao_time2 = pontuacao_time2 + 3
       
    elif(jogo1[1][2][0] == jogo1[1][2][1]):
        pontuacao_time1 = pontuacao_time1 + 1
        pontuacao_time2 = pontuacao_time2 + 1
       
    elif(jogo1[1][2][0] > jogo1[1][2][1]):
    	pontuacao_time2 = pontuacao_time2 + 3
       
    elif(jogo1[1][2][0] < jogo1[1][2][1]):
    	pontuacao_time1 = pontuacao_time1 + 3
   
	return {jogo1[0][0]:pontuacao_time1, jogo1[0][1]: pontuacao_time2}