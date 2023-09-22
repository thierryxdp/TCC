def quant_palavras(frase):
    '''Dada uma frase, a função retorna
    o número de palavras contidas na frase
    str -> int'''
    frase2 = str.split(frase," ")
    return str.count(frase2)