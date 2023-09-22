#Start your python function here
#Start your python function here
#Start your python function here
#Start your python func#Start your python function here
#Start your python function here
def pontos_por_time(pts):
    resultado = {}
    resultado[pts[0][0]] = 0
    resultado[pts[0][1]] = 0
    for jogo in pts:
        if jogo[2][0] > jogo[2][1]:
        	resultado[jogo[0]] += 3
        elif jogo[2][1] > jogo[2][0]:
            resultado[jogo[1]] += 3
        else:
            resultado[jogo[0]] += 1
            resultado[jogo[1]] += 1
    return resultado#Start your python function here#Start your python function here
#Start your python function heretion here#Start your python function here