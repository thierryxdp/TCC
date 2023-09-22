def inverte(frase):
    '''retorna a string fornecida inversa, sem pontuacao ou letras maiusculas.
    str->str'''
    frase = frase.lower()
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace('-', ' ')
    
    return ' '.join(frase.split()[::-1])