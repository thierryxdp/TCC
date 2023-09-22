def quant_palavras(frase):
    ''' retorna o número de palavras, dada uma frase como parâmetro;
    str -> int '''
    f=str.strip(frase)
    return len(str.split(f)