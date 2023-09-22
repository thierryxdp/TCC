def conta_palavras(frase):
    """calcula e retorna o numero de palavras, dado a varaivel frase; str-->int"""
    frase = str.strip(frase)
    frase = str.split(frase)
    return len(frase)