def posLetra(frase,letra,ocorrencia):
    if letra in frase and ocorrencia<str.count(frase,letra):
    	return str.index(frase,letra,ocorrencia,)
    if letra in frase and ocorrencia>str.count(frase,letra):
        return -1
    else:
        return -1