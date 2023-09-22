def posLetra(frase,letra,n_ocorrenc):
    
    indice=0
    quant_letra=str.count(frase,letra,len(frase))
    
    
    while indice<len(frase):
    	if frase[indice] in letra:
    		posicao=len(frase[:indice])
            
        elif quant_letra<n_ocorrenc:
            posicao=-1
            
        indice=indice+1
        
    return posicao