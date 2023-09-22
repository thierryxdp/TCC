def quant_palavras(frase):
    """Função que conta quantas palavras estão dentro de uma frase, dada a frase comop entrada;
    str -> int"""
    num_palavras = str.split(frase)
    return len(num_palavras)