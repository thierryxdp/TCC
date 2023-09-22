def posLetra(frase, letra, num):
    xLetras = frase.count(letra)
    ocorrencia = 0
    indice = -1
    
    if xLetras >= num:
        while ocorrencia != num:            
            if frase[indice+1::] != letra:
                indice += 1                
                    
            else:
                ocorrencia += 1
                indice += 1
                
    	return indice
  	
    else:
        retorno = -1
        return retorno