def quant_palavras(frase):
    """Dada uma frase, retorna a quantidade de palavras na frase ignorando espaços em branco.  """
    sep = frase.strip().split()
    return len(sep)