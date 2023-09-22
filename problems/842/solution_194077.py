def pontos_por_time
'Função que calcula pontos por time'
if j1t1 > j1t2 and j2t1 > j2t2:
		return {time1 : 6, time2 : 0}
	if j1t1 > j1t2 and j2t1 == j2t2:
		return {time1 : 4, time2 : 1}
	if j1t1 == j1t2 and j2t1 == j2t2:
		return {time1 : 2, time2 : 2}
	if j1t1 == j1t2 and j2t1 < j2t2:
		return {time1 : 1,time2 : 4}
	if j1t1 < j1t2 and j2t1 < j2t2:
		return {time1 : 0, time2 : 6}
    if j1t1 > j1t2 and j2t1 < j2t2:
		return {time1 : 3, time2 : 3}
	if j1t1 < j1t2 and j2t1 > j2t2:
		return {time1 : 3, time2 : 3}
	else: 
		if j1t1 == j1t2 and j2t1 > j2t2:
			return {time1: 4, time2 : 1}