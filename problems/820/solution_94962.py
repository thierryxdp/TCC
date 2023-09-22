def posLetra(frase, letra, num):
    frase = list(frase)
    xLetras = frase.count(letra)
    ocorrencia = 0
    indice = 0
    cont = 0
    
    if xLetras >= num:
        while ocorrencia != num:
           	indice = frase.index(letra)
        	ocorrencia += 1
       	 		while cont <= xLetras:
            		indice = frase[ocorrencia+1::]
                    if indice == letra:
                        ocorrencia += 1
                        cont += 1
                    
                    else:
                        pass
        frase = ''.join(frase)
       	return frase
  	
    else:
        retorno = -1
        return retorno