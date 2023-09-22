def posLetra(frase,letra,ocorrencia):
    if letra in frase:
    	return str.index(frase,letra,ocorrencia,)
    else:
        return -1