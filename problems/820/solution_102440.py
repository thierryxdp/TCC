def posLetra(frase:str,letra:str,n:int)->int:
	x=0#contador de loop
	y=0#contador de ocorrência
	while x<len(frase):
    	if frase[x]==letra: 
        	y=y+1#ocorrência de letra
    		if y==n:
        		return str.index(frase,frase[x:])#pegando o própio valor de frase em x
		x=x+1
	return -1