def quant_palavras(frase):
    """funcao que dado uma frase,retorna o numero de palavras contida nessa frase,incluindo os espaços; str -> int"""
    frase = str.split(frase)
    return len(frase)