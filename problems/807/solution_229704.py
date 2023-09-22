def conta_frases (frase):
    '''conta o número de frases que aparecem na frase; entrada é a frase;str->str'''
    frase = str.replace(frase,'. ',' ')
    frase = str.split(frase)
    return len(frase)