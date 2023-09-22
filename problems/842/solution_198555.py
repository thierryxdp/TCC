def pontos_por_time (lista):
jogo_ida = int(lista[0][2][0]) + int(lista[0][2][1]) + int(lista[1][2][0])
jogo_volta = int(lista[1][2][1]) + int(lista[2][2][0]) + int(lista[2][2][1])

total_de_pontos = jogo_ida + jogo_volta

	return total_de_pontos