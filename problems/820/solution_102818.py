def posLetra(frase,letra,n):
    #contador
    pos=0
    ocor=0
    #caso menos ocorrencia retornar -1
    #if(frase.count(letra) < n or frase.count(letra)==0):
    #   return -1
       
    while(pos<len(frase)):
        if(frase[pos]==letra):
            ocor+=1
        	if (ocor==n):
            	return pos
        pos+=1        
                  
    return -1