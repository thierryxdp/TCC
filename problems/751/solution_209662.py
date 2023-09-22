def quant_palavras(frase):
    """retorna em int a quantidade de palavras dentro de uma str
    str->int"""
    return str.count(str.strip(frase),' ')+1