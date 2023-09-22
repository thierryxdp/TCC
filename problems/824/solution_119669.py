def uppcons(frases):
    '''dada uma frase com consoantes e retorne a frases com consoantes em maiusculo
    :param frase: str->str
    :return: str->str'''
    
    contador= 0
    novafrase= ()
    while contador < len(frase):
        if frase[contador] not in 'aeiouãéíóúAEIOU':
            novafrase += frase[contador].upper()
        else: 
            novafrase += frase[contador].lower()
            contador +=1   
        return novafrase