def posLetra(frase,letra,ocorrencia):
    i=0
    LetraI=0
    while i<=ocorrencia:
        LetraI=frase.find(letra,LetraI)
        if LetraI==-1:
        	break
        
    return LetraI