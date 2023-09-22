#Start your python function here
def pontos_por_time(K):
  
	def pontos(A,B):
    	if (A>B):
      		return 3
    	if (A<B):
      		return 0
    	if (A==B):
      		return 1

 	placar1 = K[0][1]
 	placar2 = K[1][1]
 	time1   = K[0][0][0]
 	time2   = K[0][0][1]

 	pontos_time_1 = pontos(placar1[0],placar1[1]) + pontos(placar2[1],placar2[0])
 	pontos_time_2 = pontos(placar1[1],placar1[0]) + pontos(placar2[0],placar2[1])

 	return {time1:pontos_time_1, time2:pontos_time_2}