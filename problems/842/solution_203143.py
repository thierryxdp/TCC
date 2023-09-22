def pontos_por_time (L):
    '''essa funçao recebe uma lista com informaçoes dos gols de dois times no jogo de ida e no 
    de volta, e retorna um dicionario com o total de pontos de cada time
    lista (str, int) -> bool'''
    
    #L= [[time1,time2, [gol1,gol2], [time2, time1, [gol2, gol1]]
    
    p1=0
    p2=0
    
	if L[0][2][0] > L[0][2][1]:
        p1=p1+3
        
	elif L[0][2][0] < L [0][2][1]:
        p2=p2+3
            
	else:
        p1=p1+1
        p2=p2+1
            
                            
	if L[1][2][0] > L[1][2][1]:
        p2=p2+3
             
	elif L[1][2][0] < L[1][2][1]:
        p1=p1+3
             
	else:
        p1=p1+1
        p2=p2+1
    
           
	return {L[0][0]: p1, L[0][1] : p2}