#Start your python function here
def pontos_por_time([[[Time1,Time2,[JogoIda]],[Time2,Time1,[JogoVolta]]]):
    if JogoIda[0] != JogoIda[1]:
        if JogoIda[0] > JogoIda[1]:
        	PontoTime1Ida = 3
    	elif JogoIda[0] < JogoIda[1]:
        	PontoTime2Ida = 3
    	elif JogoIda[0] == JogoIda[1]:
       		PontoTime1Ida = PontoTime2Ida = 1
    
    elif JogoVoltA[0] != JogoVolta[1]:
        if JogoVolta[0] > JogoVolta[1]:
        	PontoTime2Volta = 3
    	elif JogoVolta[0] < JogoVolta[1]:
        	PontoTime1Volta = 3
    	elif JogoVolta[0] == JogoVolta[1]:
        	PontoTime1Volta = PontoTime2Volta = 1
    else:
        PontoTime1Ida = PontoTime2Ida = 0
        PontoTime1Volta = PontoTime2Volta = 0
       
    return {str(Time1) : PontoTime1Ida + PontoTime1Volta, str(Time2) : PontoTime2Ida + PontoTime2Volta}