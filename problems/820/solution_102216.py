def posLetra(frase,letra,n):
    """
    
    """
    i=0
    repeticoes=""
    resposta=""
    while n!=len(repeticoes)+1:
        if i==len(frase):
            resposta=-1
            n=len(repeticoes)
        elif frase[i]==letra:
            repeticoes+=letra
            i+=1
            resposta=len(repeticoes)
	return resposta