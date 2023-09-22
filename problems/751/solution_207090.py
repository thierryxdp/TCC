t
def quant_palavras(frase):
    """Dada uma frase retorna a quantidade de palavras dela ignorando os espaços em branco
       str -> int   """
    sep = frase.strip().split()
    return len(sep)