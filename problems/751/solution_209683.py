def quant_palavras(frase):
    
    '''A função calculará a quantidade de palavras escritas em uma frase.
    parâmetros de entrada -> string
    parâmetros de saída -> int
    '''
    x = str.split(frase," ")
    y = len(x)
    
    return y