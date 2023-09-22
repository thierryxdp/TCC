def quant_palavras (frase):
    '''entrada: 'frase'
       função que calcula quantas palavras compõem a frase
       enviada e retorna a quantidade
       [str-->int]'''
    return len(str.split(str.strip(frase)))