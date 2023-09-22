def quant_palavras(frase):
    """ Função que dada uma frase, retorna o numero de palavras da frase.
    string -> int
    """
    x=frase.strip()
    return len(x.split(' '))