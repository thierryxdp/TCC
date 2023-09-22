def pontos_por_time ():
	''' funcao que recebe uma lista de dois elementos onde cada um desses elementos tambem seja uma lista;
list -> dict '''
	numero_gols = [['Cormengo', 'Flaminthias', [1, 0]], 'Flaminthias', 'Cormengo', [2,2]]
	vitoria = 3
	empate = 1
	derrota = 0
	return {'Cormengo':(vitoria + empate), 'Flaminthias':(empate)};