#Start your python function here
def pontos_por_time(lista):
    l1 = lista[0]
    l2 = lista[1]
    
    rodada1 = l1[2]
    rodada2 = l2[2]
    
    time1 = l1[0]
    time2 = l1[1]
    
   	if rodada1[0] > rodada1[1]:
        pts1 = 3
        pts2 = 0
   	elif rodada1[0] == rodada1[1]:
        pts1 = 1
        pts2 = 1
 	else:
        pts1 = 0
        pts2 = 3
   	if rodada2[0] > rodada2[1]:
        pts1 = pts1 + 3
        pts2 = pts2 + 0
    elif rodada2[0] == rodada2[1]:
        pts1 = pts1 + 1
        pts2 = pts2 + 1
    else:
        pts1 = pts1 + 0
        pts2 = pts2 + 3
   	
    return {time1 : pts1, time2 : pts2}