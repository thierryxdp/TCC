def quant_palavras(frase):
    ''' retorna o número de palavras, dada uma frase como parâmetro;
    str -> int '''
    x = str.strip(frase)
    return (len(str.split(x)))