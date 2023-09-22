a funcao retorna seu numero de palavras
def quant_palavras(frase):
    """a funcao recebe uma frase e retorna o seu numero de palavras """
    frase=str.split(frase)
    return len(frase)