def quant_palavras(frase):
    """A função recebe uma frase e retorna o numero de palavras dela;
    Str -> Int"""
    a = str.split (frase, ' ')
    if '' in a:
        list.remove (a, '')
    return len(a)