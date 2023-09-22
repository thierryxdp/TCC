def posLetra(texto,letra,ocorrencia):
    '''str,str,int -> int'''
    i = 1
    contadorFinal = 0
    numerodeocorrencias = 0
    if letra not in texto or texto.count(letra) < ocorrencia:        
        return -1
    else:        
    	while numerodeocorrencias < ocorrencia:        
        	contadorFinal = texto[i:].find(letra)
        	i = contadorFinal
            numerodeocorrencias += 1   	    
    return contadorFinal