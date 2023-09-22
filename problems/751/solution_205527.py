def quant_palavras (frase):
    ''' função que, dada uma frase, retorna o número de palavras da
    frase; str -> int'''
    return str.count((str.strip(frase)), " ") + 1