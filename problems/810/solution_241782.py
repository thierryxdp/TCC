def inverte(frase):
    fraseF = frase.split('!')
    fraseF = frase.split('?')
    fraseF = frase.split('.')
    fraseF = frase.split(',')
    return ''.join(str.lower(fraseF[::-1]))