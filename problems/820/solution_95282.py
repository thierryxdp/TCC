def posLetra(string,letra,ocorrencia):
    quantidadeletras = str.count(string,letra)
    contador = 1
    if quantidadeletras < ocorrencia:
        return -1
    else:
        while contador < ocorrencia:
            string = str.replace(string,letra,'#',1)
            contador = contador + 1
    	return str.index(string,letra)