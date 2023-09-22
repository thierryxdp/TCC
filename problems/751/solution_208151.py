def quant_palavras(frase):
    '''Dada uma frase, retorna o número de palavras da frase. string-->float'''
    frase = frase.strip("")
    frase = frase.split("")
    return len(frase)