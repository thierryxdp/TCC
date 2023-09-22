def quant_palavras(frase):
    """A função verifica quantas frases ou conjunto de palavras existem, que constitui a frase completa
    string -> int"""
    
    x = str.split(str.strip(frase))
    
    return len(x)