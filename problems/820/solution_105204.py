def posLetra(texto,letra,ocorrencia):
    '''str,str,int -> int'''
    i = ''
    contadorFinal = 0
    numerodeocorrencias = len(i)
    if letra not in texto or texto.count(letra) < ocorrencia:
        return -1
    else:        
    	while numerodeocorrencias < len(texto):        
        	contadorFinal = texto[i:].find(letra)
        	i = texto[contadorFinal:]
   	    return contadorFinal