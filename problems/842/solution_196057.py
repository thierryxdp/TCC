def pontos_por_time (jogos):
    """Função que dada duas listas dos jogos de ida e de volta retorna o número total de pontos de cada time
    entrada:list
    saída:dict"""
    jogos=[['time1','time2',['placar']],['time2','time1',['placar']]]
   		if jogos[0][2][0]>jogos[0][2][1] and jogos[1][2][1]>jogos[1][2][0]:
        	pt1=6
        	pt2=0
    	elif jogos[0][2][1]>jogos[0][2][0] and jogos [1][2][0]>jogos[1][2][1]:
        	pt1=0
        	pt2=6
    	elif jogos[0][2][0]>jogos[0][2][1] and jogos[1][2][1]==jogos[1][2][0] or jogos[0][2][0]==jogos[0][2][1] and jogos[1][2][1]>jogos[1][2][0]:
        	pt1=4
        	pt2=1
    	elif jogos[0][2][1]>jogos[0][2][0] and jogos[1][2][0]==jogos[1][2][1] or jogos[0][2][1]==jogos[0][2][0] and jogos[1][2][0]>jogos[1][2][1]:
        	pt1=1
        	pt4=4
    	elif jogos[0][2][0]>jogos[0][2][1] and jogos[1][2][1]<jogos[1][2][0] or jogos[0][2][0]<jogos[0][2][1] and jogos[1][2][1]>jogos[1][2][0]:
        	pt1=3
        	pt2=3
    	else:
        	pt1=2
        	pt2=2
    return {'time1':pt1,'time2':pt2}