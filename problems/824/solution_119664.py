def uppcons(frases):
    '''dada uma frase com consoantes e retorne a frases com consoantes em maiusculo
    :param frase: str->str
    :return: str->str'''
    
    contador= 0
    novafrase= ' '
    while contador < len(frase):
        if frase[contador] not in 'aeiouãéíóú':
            novafrase += frase[contador].upper()
            
        return novafrase