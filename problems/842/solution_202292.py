#Start your python function here
def detecta_empate(placar):
    if placar[2][0] = placar[2][1]:
        return "empate"
    elif placar[2][0] > placar[2][1]:
        return placar[0]
    elif placar[2][0] < placar[2][1]:
        return placar[1]

def pontos_por_time(lista):
    d= {lista[0][0]:0
    lista[0][1]:0}
    for placar in lista:
        if detecta_empate(placar) == "empate":
            d[placar[0]] += 1
            d[placar[1]] += 1
        else:
            d[detecta_empate(placar)] += 1
	return d