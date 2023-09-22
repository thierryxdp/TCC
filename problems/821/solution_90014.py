def fatorial(x):
	contador = 0
    resposta = 1
    while (x-contador)>1:
    	resposta*= (x-contador)
        contador+=1
        
	return resposta