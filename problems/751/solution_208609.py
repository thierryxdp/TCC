def quant_palavras(frase):
    """Retorna a quantidade de palavras que existem em uma frase. 
    Str -> Int"""
    frase_copia = frase[:]
    palavras = str.split(frase_copia)
    return len(palavras)