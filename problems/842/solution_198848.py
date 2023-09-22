[['Cormengo','Flamínthians', [1, 0]],['Flamínthians', 'Cormengo', [2, 2]]]


# função que mostra o total de pontos de duas partidas uma em casa e outra fora de casa 
# list-->dicionario
def pontos_por_time(p):
	x = p[0] # ['Cormengo', 'Flamínthians', [1, 0]]
	y = p[1] # ['Flamínthians', 'Cormengo', [2, 2]]

	pp = x[2]# [1, 0]
	sp = y[2]# [2, 2]
	
	time1 = x[0]#['Cormengo']
	time2 = y[0]#['Flamínthians']
	
	if pp[0] < pp[1] and sp[0] > sp[1]:
		return {time2: 6, time1: 0}
	if pp[0] > pp[1] and sp[0] < sp[1]:
		return {time1: 6,time2: 0}
	if pp[0] < pp[1] and sp[0] == sp[1]:
		return {time2: 4,time1: 1}
	if pp[0] > pp[1] and sp[0] == sp[1]:
		return {time1: 4,time2: 1}
	if pp[0] == pp[1] and sp[0] < sp[1]:
		return {time1: 4,time2: 1}
	if pp[0] == pp[1] and sp[0] > sp[1]:
		return {time2: 4,time1: 1}
	if pp[0] < pp[1] and sp[0] < sp[1]:
		return {time2: 3, time1: 3}
	if pp[0] > pp[1] and sp[0] > sp[1]:
		return {time1: 3, time2: 3}
	if pp[0] == pp[1] and sp[0] == sp[1]:
		return {time1: 2,time2: 2}