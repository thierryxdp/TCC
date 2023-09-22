def posLetra(frase,letra,ocorrencia):
    i=0
    LI=0
    while i<len(frase):
        i=i+1
        LI=0
        LI= frase.find(letra,LI,len(frase))
        if LI== ocorrencia:
        	return LI