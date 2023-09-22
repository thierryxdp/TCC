#Considere que a frase pode ter espaços no início e no final
def quant_palavras(frase):
    """Função que dada uma frase, retorna o n° de palavras
    da frase;
    str -> int"""
    removeSpaces = frase.strip()
    splitPhrase = removeSpaces.split()
    return len(splitPhrase)