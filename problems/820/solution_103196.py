def posLetra(frase,letra,n):
    """Dada a frase de entrada, a letra e a posição n, retorne em que posição da string aquela ocorrência da letra está"""
    posição = frase.find(letra)
    while posição>=0 and n>1:
        if letra!=frase:
            posição = frase.find(letra,posição+1)
        n = n + 1
    return posição