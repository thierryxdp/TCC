def quant_palavras(frase):
    """A função recebe uma frase e retorna o numero de palavras dela; Str -> Int"""
    separada = str.split (frase, ' ')
    if '' in separada:
        list.remove (separada, '')
    return len(a)