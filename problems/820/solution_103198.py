def posLetra(frase,letra,n):
    """Dada a frase de entrada, a letra e a posição n, retorne em que posição da string aquela ocorrência da letra está"""
    posicao = frase.find(letra)
    while posicao>=0 and n>1:
        if letra!=frase:
            posicao = frase.find(letra,posicao+1)
        n = n + 1
    return posicao