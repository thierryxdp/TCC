def posLetra(frase, letra, ocorrencia):
    """Essa funcao, dada uma string, uma letra e um numero que indica uma ocorrencia,
	 retorna em que posicao da string aquela ocorrencia da letra esta.
     str -> int"""
    i = 0
    o = 0
    while i < len(frase):
        if frase[i] == letra:
            o = o + 1
            if o == ocorrencia:
                return frase.index(frase[i], i)
        i = i + 1
    else:
        return -1