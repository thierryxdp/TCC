def quant_palavras(frase):
    ''' Dada uma frase, retorna a quantidade de palavras
    contidas na frase
    str -> int'''
    lista_palavras = str.split(frase)
    numero= len(lista_palavras)
    return numero