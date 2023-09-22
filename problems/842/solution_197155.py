#Start your python function here
def pontos_por_time(dia1):
    time1 = 0
    time2 = 0
    
    if (dia1[0][2][0] > dia1[0][2][1]):
        time1 += 3
	elif (dia1[0][2][0] < dia1[0][2][1]):
    	time2 += 3      
         
    return time1, time2