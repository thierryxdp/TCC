def conta_frases (frase):
    '''conta o número de frases que
    aparecem na frase; entrada é a frase;str->str'''
    frase1= str.split(frase,'!')
    return len(frase1)