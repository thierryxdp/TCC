#Start your python function here]
def pontos_por_time(pts):
    resultado = {}
    for jogo in pts:
        if jogo[2][0] > jogo[2][1]:
        	resultado[jogo[0]] += 3
        elif jogo[2][1] > jogo[2][0]:
            resultado[jogo[1]] += 3
        else:
            resultado[jogo[0]] += 1
            resultado[jogo[1]] += 1
    return resultado