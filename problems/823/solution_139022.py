def faltante(L):
    posicao = 0
    while posicao < len(L):
    	if posicao+1 == L[posicao]:
    posicao = posicao + 1    
    return posicao+1