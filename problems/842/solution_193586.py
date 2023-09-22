def pontos_por_time(_l):
	pontos1 = [_l[0][2][0], _l[1][2][0]]
    pontos2 = [_l[0][2][1], _l[1][2][1]]
    t1 = [_l[0][0], 0]
    t2 = [_l[1][0], 0]
    
    if pontos1[0] == pontos2[0]:
    	t1[1] += 1
		t2[1] += 1
	elif pontos1[0] >= pontos2[0]:
    	t1[1] += 3
	elif pontos1[0] <= pontos2[0]:
   	    t2[1] += 3
 	
	if pontos1[1] == pontos2[1]:
   	 	t1[1] += 1
		t2[1] += 1
	elif pontos1[1] >= pontos2[1]:
		t2[1] += 3
	elif pontos1[1] <= pontos2[1]:
 		t1[1] += 3
   	
   	return {t1[0]:t1[1], t2[0]:t2[1]}