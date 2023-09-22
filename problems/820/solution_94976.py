def posLetra(frase, letra, num):
    frase = list(frase)
    xLetras = frase.count(letra)
    ocorrencia = 0
    indice = -1
    
    if xLetras >= num:
        while ocorrencia != num:
            cont = frase[indice+1::]
            if cont == letra:
                indice += 1
                ocorrencia += 1
                    
            else:
                indice += 1
                
    	return indice
  	
    else:
        retorno = -1
        return retorno