def conta_frases (frase):
    '''conta o número de frases que aparecem na frase; entrada é a frase;str->str'''
    frase1 = str.replace(frase,'. ',' ')
    frase2 = str.split(frase1)
    return len(frase2)