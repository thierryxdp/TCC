def pontos_por_time(lista):
    d={}
   
	jogo_1 = {"time1": lista[0][0],"golcasa": lista[0][2][0],
       "time2": lista[0][1], "golfora":lista[0][2][1]}
    
    jogo_2 = {"time1": lista[1][0], "golcasa": lista[1][2][0],
              "time2": lista[1][1], "golfora": lista[1][2][1]}
    
    if jogo_1.get("golcasa") > jogo_1.get("golfora"):
   #     d["time1"]=3
		return (jogo_1.["golcasa])