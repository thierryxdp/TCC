def conta_frases(frase):
    """
    Faca uma funcao que dada uma frase, retorne o numero de palavras da frase. 
    Considere que a frase pode ter espacos no inicio e no final.
    """
    #frase = str.strip(frase)
    frase = str.split(frase)
    return len(frase)