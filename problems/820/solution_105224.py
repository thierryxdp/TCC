def posLetra(frase,letra,ocorrencia):
    i=0
    LetraI=0
    while i<=ocorrencia:
        LetraI=str.index(frase,letra,LetraI,len(frase)-1)
        if LetraI==ocorrencia:
            break
		i+=1
    return LetraI