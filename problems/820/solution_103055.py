def posLetra(string,letra,n):
	i=0
    indice=0
    while i<len(string):
        if letra not in string:
            return -1
    	x=str.find(string,letra)
        indice=indice+x
    	i=i+0
    return indice