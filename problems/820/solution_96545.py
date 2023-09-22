def posLetra(frase,letra,n_ocorrenc):
    
    indice=0
       
    
    while indice<len(frase):
    	if frase[indice] in letra:
    		posicao=len(frase[:indice])
            
        indice=indice+1
        
    return posicao