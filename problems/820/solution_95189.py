def posLetra(string,letra,ocorrencia):
    quantidadeletras = str.count(string,letra)
    contador = 1
    if quantidadeletras < ocorrencia:
        return -1
    else:
        while contador <= ocorrencia:
            contador = contador + 1
        	a = str.index(string,letra)
    	return a