def pontos_por_time(lista):
    
	v=3
	e=1
    
	jogo_1 = {"time1": lista[0][0],"golcasa": lista[0][2][0],
       "time2": lista[0][1], "golfora":lista[0][2][1]}
    
    jogo_2 = {"time1": lista[1][0], "golcasa": lista[1][2][0],
              "time2": lista[1][1], "golfora": lista[1][2][1]}
    
	if jogo_1.get("golcasa") > jogo_1.get("golfora") and jogo_2.get("golfora") > jogo_2.get("golcasa"):
		A={jogo_1["time2"]: 0, jogo_1["time1"]: v+v}
        return A
    elif jogo_1.get("golfora") > jogo_1.get("golcasa") and jogo_2.get("golcasa") > jogo_2.get("golfora"):
		B={jogo_1["time2"]: v+v, jogo_1["time1"]: 0}
		return B