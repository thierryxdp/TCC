def pontos_por_time (jogoida,jogovolta):
	
	

	if jogoida[1][0] > jogoida[1][1]:
 		t1 = 3 
	elif jogoida[1][0] == jogoida[1][1]:
		t1 = 1
		t2 = 1
	else:
		t2 = 3

	if jogovolta[1][1] > jogovolta[1][0]:
 		t2 += 3 
	elif jogovolta[1][1] == jogovolta[1][0]:
		t1 += 1
		t2 += 1
	else:
		t1 += 3

	pontos_na_fase = {jogoida[0][0]: t1 , jogovolta[0][1]:t2}

	return pontos_na_fase{jogoida[0][0]: t1 , jogovolta[0][1]:t2}