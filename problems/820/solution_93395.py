def posLetra(texto, letra, ocorrencia):
    """retorna em que posicao do texto a ocorrencia da letra esta"""
    """str, str, int -> int"""
    if ocorrencia > str.count(texto, letra):
        return -1
    else:
        return str.index(texto, letra)