def quant_palavras(frase):
    """Essa função recebe como argumento uma string e transforma ela em uma lista de palavras,
    após retorna a quantidade de palavras nesta lista."""
    txt = frase
    a = txt.split()
    return len(a)