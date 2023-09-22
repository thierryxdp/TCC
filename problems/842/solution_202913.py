def calculaPontos(golsArray, index):
    if (golsArray[index] > golsArray[1 -index]):
        return 3
    if (golsArray[index] < golsArray[1 -index]):
        return 0
    else:
        return 1
    

 
def pontos_por_time(jogos):
	resultado = {}
	for x in jogos:
	    for y in range(2):
	        if(x[y] in resultado):
	            resultado[x[y]]+=calculaPontos(x[2],y)
	        else:
	            resultado[x[y]]=calculaPontos(x[2],y)

	   
	   
	return resultado