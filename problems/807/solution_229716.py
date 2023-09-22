def conta_frases (frase):
    '''conta o número de frases que
    aparecem na frase; entrada é a frase;str->str'''
    frase = str.split(frase, "!")
    frase = str.join(" ", frase)
    return len(frase)