def posLetra(texto,letra,ocorrencia):
    '''str,str,int -> int'''
    i = 1
    contadorFinal = 0
    numerodeocorrencias = 0
    if letra not in texto or texto.count(letra) < ocorrencia:
        return -1
    else:        
    	while 1 < len(texto):        
        	contadorFinal = texto[i:].find(letra)
        	i = texto[contadorFinal:]
   	    return contadorFinal