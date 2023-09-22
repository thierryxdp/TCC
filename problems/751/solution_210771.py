def quant_palavras(frase):
    """A função recebe uma frase e retorna a quantidade de palavras na frase.
    Assinatura: string -> int"""
    frase = str.split(frase)
    return len(frase)