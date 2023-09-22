def quant_palavras(frase):
    frase1 = frase[:]
    """Retorna a quantidade de palavras que existem em uma frase. Str -> Int"""
    palavras = str.split(frase1)
    return len(palavras)