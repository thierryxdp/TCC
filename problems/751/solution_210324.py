def quant_palavras(frase):
    """Função que, dada uma frase, retorna o número de palavras da frase.
    string -> int"""
    palavras = str.split(frase)
    return len(palavras)