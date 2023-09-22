def quant_palavras(frase):
    '''Função que dada uma frase:
    retorne o número de palavras da frase considerando seus espaços.
    str-> int'''
    frase = frase.strip()
    frase = frase.split()
    return len(frase)