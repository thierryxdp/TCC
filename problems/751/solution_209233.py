help str.split
help str.count

def quant_palavras(frase):
    '''funçao que calcula e retorna o numero de palavras em uma frase. strimg->int'''
    frase_nova=str.split(frase)
    return str.count(frase_nova)