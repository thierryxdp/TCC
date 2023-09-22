def posLetra(string,letra,ocorrencia):
    quantidadeletras = str.count(string,letra)
    contador = 0
    novafrase = ''
    if quantidadeletras < ocorrencia:
        return -1
    else:
        while contador < ocorrencia:
            novafrase = str.replace(string,letra,'#',1)
            contador = contador + 1
    	return str.index(novafrase,letra)