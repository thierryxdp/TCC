def posLetra(frase,letra,n):
    a=str.count(frase,letra)
    if a-n<0:
        return -1
    else:
    	return str.fin(frase, letra)