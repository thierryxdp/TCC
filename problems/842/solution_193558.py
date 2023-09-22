#Start your python function here
def pontos_por_time(lista):
    if lista[0][2][0] > lista[0][2][1]:
        time1 = 3
        return
	elif (lista[1][2][0] > lista[1][2][1]):
        return time2 = 3
    elif lista[0][2][0] == lista[0][2][1]:
        return time1 = 1 + time1
        return time2 = 1 + time2
	elif lista[1][2][0] == lista[1][2][1]:
        return time1 = 1 + time1
        return time2 = 1 + time2
	if time1 > time2:
        return str(lista[0][0])+": "+time1, str(lista[0][1])+": "+time2
    else:
        return lista[0][1]+': '+time2, lista[0][0]+': '+time1