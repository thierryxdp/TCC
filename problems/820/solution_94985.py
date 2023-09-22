def posLetra(frase, letra, num):
    frase = list(frase)
    xLetras = frase.count(letra)
    ocorrencia = 0
    indice = -1
    cont = ''
    
    if xLetras >= num:
        while ocorrencia != num:
            
            cont = str(frase[indice+1::])
            
            if cont != letra:
                indice += 1                
                    
            else:
                ocorrencia += 1
                indice += 1
                
    	return indice
  	
    else:
        retorno = -1
        return retorno