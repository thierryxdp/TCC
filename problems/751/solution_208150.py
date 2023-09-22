def quant_palavras(frase):
    '''Dada uma frase, retorna o número de palavras da frase. string-->float'''
    frase = frase.split("")
    frase = frase.strip("")
    return len(frase)