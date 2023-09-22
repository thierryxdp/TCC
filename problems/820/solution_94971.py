def posLetra(frase, letra, num):
    frase = list(frase)
    xLetras = frase.count(letra)
    ocorrencia = 0
    indice = 0
    cont = -1
    
    if xLetras >= num:
        while ocorrencia != num:
            indice = frase[indice+1::]
            if indice == letra:
                ocorrencia += 1
                    
            else:
                pass
                
       	return indice
  	
    else:
        retorno = -1
        return retorno