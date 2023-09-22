def posLetra(f,l,n):
    i = 0
    resultado = 0
    while i < len(f):
    	if len(f[i]) == n:
    		resultado = resultado + len(f[i])
        else:
            resultado = -1
    	i = i + +1
    return resultado