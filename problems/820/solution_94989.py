def posLetra(frase, letra, num):
    frase = frase.split(str)
    xLetras = frase.count(letra)
    ocorrencia = 0
    indice = -1
    cont = ''
    
    if xLetras >= num:
        while ocorrencia != num:            
            letraTeste = str(frase[indice+1::])
            
            if letraTeste != letra:
                indice += 1                
                    
            else:
                ocorrencia += 1
                indice += 1
                
    	return indice
  	
    else:
        retorno = -1
        return retorno