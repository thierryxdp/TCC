def retura_pontuacao(frase):
    frase = frase.split('-')
    frase = ''.join(frase)
    frase = frase.split(',')
    frase = ''.join(frase)
    frase = frase.split(':')
    frase = ''.join(frase)
    frase = frase.split(';')
    frase = ''.join(frase)
    frase = frase.split(.)
    frase = ''.join(frase)
    return frase