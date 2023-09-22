def quant_palavras(frase):
    '''dado uma frase com espaços calcula a quantidade de plavras+ espaço e dimunui os espaços, retornando apenas a quantidade de palavras'''
    ''' Str-> int'''
    return len(frase)- str.count(frase,' ',0)