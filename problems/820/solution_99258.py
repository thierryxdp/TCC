def posLetra(frase,letra,pos):
    if letra in frase:
        
    	local = frase.index(letra,pos-1,pos+1)
    else:
        return -1