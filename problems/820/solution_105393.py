def posLetra(texto,letra,ocorrencia):
    """retorna o indice de determinada ocorrencia 
    da letra dada
    str,str,int --> int"""
    if  0 < ocorrencia <= texto.count(letra):
        i = 0
        while ocorrencia > 0:
            i = texto.find(letra,i)
            ocorrencia -= 1
    	return i
	return -1