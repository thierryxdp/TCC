def pontos_por_time(lista):
   
	jogo_1 = {"time1": lista[0][0],"golcasa": lista[0][2][0],
       "time2": lista[0][1], "golfora":lista[0][2][1]}
    
    jogo_2 = {"1time": lista[1][0], "casagol": lista[1][2][0],
              "2time": lista[1][1], "foragol": lista[1][2][1]}
    
    return jogo_1, jogo_2