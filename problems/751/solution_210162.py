def quant_palavras(frase):
    '''Dada uma frase, a função retorna
    o número de palavras contidas na frase
    str -> int'''
    return str.count(str.split(frase),frase)