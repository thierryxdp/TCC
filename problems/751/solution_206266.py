def quant_palavras(frase):
    '''função que recebe uma frase e retorna a quantidade de palavras existentes na frase.
    str -> int'''
    s = frase
    return len(str.split(s))