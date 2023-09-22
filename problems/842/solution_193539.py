#Start your python function here
def pontos_por_time(lista):
   	if lista[0][2][0] > lista[0][2][1]:
		time1 = 3 + time1
	if lista[1][2][0] > lista[1][2][1]:
        time2 = 3 + time2
    if lista[0][2][0] == lista[0][2][1]:
        time1 = 1 + time1
        time2 = 1 + time2
	if lista[1][2][0] == lista[1][2][1]:
        time1 = 1 + time1
        time2 = 1 + time2
	if time1 > time2:
        return lista[0][0]+': '+time1, lista[0][1]+': 'time2
    else:
        return lista[0][1]+': '+time2, lista[0][0]+': 'time1