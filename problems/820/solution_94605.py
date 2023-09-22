def posLetra(frase, letra, ocorrencia):
    """RGDG"""
    i = 0
    o = 0
    while i < len(frase):
        if frase[i] == letra:
            o = o + 1
            if o == ocorrencia:
                return frase.index(string[i], i)
        i = i + 1
    else:
        return -1