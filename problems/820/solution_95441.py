def posLetra(frase,letra,ocorrencia):

    indice = 0
    contador = 0

    while indice < len(frase):
                                
        if contador == ocorrencia:
            return indice 
	            
        elif frase[indice] == letra:       
            contador += 1
            indice += 1
	        
        else:
            indice = indice + 1