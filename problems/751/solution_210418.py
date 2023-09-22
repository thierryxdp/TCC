def quant_palavras(frase):
    """retorna a quantidade de palavras numa frase tirando espaços"""
    acentos1 = frase.replace("!", "")
    acentos2 = acentos1.replace("?", "")
    acentos3 = acentos2.replace(".", "")
    mid = acentos3.split()
    return len(mid)