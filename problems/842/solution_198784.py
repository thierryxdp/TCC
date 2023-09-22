# função que mostra o total de pontos de duas partidas uma em casa e outra fora de casa 
# list-->dicionario
def pontos_por_time(casa, fora):
	partida1= pontos_por_time(casa)
	partida2= pontos_por_time(fora)

	pp = partida1[2]
	sp = partida2[2]

	if pp[0] < pp[1] and sp[0] < sp[1]:
		return {'Flamínthians': 6,'Cormengo': 0}
	if pp[0] > pp[1] and sp[0] > sp[1]:
		return {'Cormengo': 6,'Flamínthians': 0}
	if pp[0] < pp[1] and sp[0] == sp[1]:
		return {'Flamínthians': 4,'Cormengo': 1}
	if pp[0] > pp[1] and sp[0] == sp[1]:
		return {'Cormengo': 4,'Flamínthians': 1}
	if pp[0] == pp[1] and sp[0] == sp[1]:
		return {'Cormengo': 2,'Flamínthians': 2}
	if pp[0] == pp[1] and sp[0] < sp[1]:
		return {'Flamínthians': 4,'Cormengo': 1}
	if pp[0] == pp[1] and sp[0] > sp[1]:
		return {'Cormengo': 4,'Flamínthians': 1}