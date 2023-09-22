def quant_palavras(frase):
    '''função que recebe uma frase e retorna o número de palavras nela.
    entrada:string
    saída: int'''
    frase_dividida = str.split(frase)
    return str.count(frase_dividida,[:])