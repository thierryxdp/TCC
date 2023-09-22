partida1= (casa)['Cormengo','Flamínthians', [1, 0]]
partida2= (fora_de_casa)['Flamínthians', 'Cormengo', [2, 2]]

# função que mostra o total de pontos de duas partidas uma em casa e outra fora de casa 
# list-->dicionario
def pontos_por_time(x):
	partida1= x[0]
	partida2= x[1]

	pp = partida1[2]
	sp = partida2[2]
	time1 = partida1[0]
	time2 = partida1[1]
	if pp[0] < pp[1] and sp[0] < sp[1]:
		return {time2: 6, time1: 0}
	if pp[0] > pp[1] and sp[0] > sp[1]:
		return {time1: 6,time2: 0}
	if pp[0] < pp[1] and sp[0] == sp[1]:
		return {time2: 4,time1: 1}
	if pp[0] > pp[1] and sp[0] == sp[1]:
		return {time1: 4,time2: 1}
	if pp[0] == pp[1] and sp[0] == sp[1]:
		return {time1: 2,time2: 2}
	if pp[0] == pp[1] and sp[0] < sp[1]:
		return {time2: 4,time1: 1}
	if pp[0] == pp[1] and sp[0] > sp[1]:
		return {time1: 4,time2: 1}