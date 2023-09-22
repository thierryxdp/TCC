def posLetra(frase,letra,n_ocorrenc):
    
    indice=0
    quant_letra=str.count(frase,letra)
    
    
    while indice<len(frase):
    	if frase[indice] in letra:
    		posicao=str.find(frase,frase[indice])
            
        indice=indice+1
        
    return posicao