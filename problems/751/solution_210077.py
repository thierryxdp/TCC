def quant_palavras(frase):
    """Funçao que retorna a quantidades de palvaras dada uma frase como valor de entrada
    str->int"""
    quantidade_de_palavras = str.split(frase)
    return len(quantidade_de_palavras)