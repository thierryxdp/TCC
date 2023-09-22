def posLetra(string, letra, ocorrencia):
    """A função recebe como entrada uma string, outra string
    correspondente a uma letra e um inteiro correspondente
    ao número ordinal da ocorrência da letra na string e retorna
    o índice de posição dessa ocorrência."""
    
    i = 0
    vezes = 0
    while i < len(string):
        if letra == string[i]:
            vezes += 1
            i += 1
        else:
            i +=1
        if vezes == ocorrencia:
            return i - 1
        if vezes > ocorrencia:
            return -1
    return i