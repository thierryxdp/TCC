def pontos_por_time(x):
    r = {}
    time1 = [0]
    time2 = [0]
    if x[0][2][0] > x[0][2][1]:
        time1 = time1 + [3]
	elif x[0][2][0] < x[0][2][1]:
        time2 = time2 + [3]
	elif x[0][2][0] == x[0][2][1]:
        time1 = time1 + [1]
        time2 = time2 + [1]
	
    return time2