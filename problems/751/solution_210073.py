def quant_palavras(frase):
    '''a funcao retorna o número de palavras da frase
str -> int'''
    if frase[0]==" " and frase[-1]==" ":
        return str.count(frase," ", 0, len(frase)) -1
    if frase[0]==" " or frase[-1]==" ":
        return str.count(frase," ", 0, len(frase))
    else:
        return str.count(frase," ", 0, len(frase))+1