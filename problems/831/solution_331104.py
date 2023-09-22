def lingua_p(frase):
    frasen=""
    str.lower(frase)#transformar em minúsculo
	for x in (frase):#varre o vetor
        if x in "áaéeiíóouú":#compara a letra
            x=x+"p"+x #faz substituição 
    	
    	
    	frasen=frasen+x
            
	return frasen