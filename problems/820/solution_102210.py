def posLetra(frase,letra,n):
    """
    
    """
    i=0
    repeticoes=""
    resposta=len(repeticoes)
    while n!=len(repeticoes):
        if i==len(frase):
            resposta=-1
            n=len(repeticoes)
        if frase[i]==letra:
            repeticoes+=letra
            i+=1        
	return resposta