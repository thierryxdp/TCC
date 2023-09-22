def conta_frases(frase):
    """Essa função conta o número de frases no texto. Considera-se
    o final de uma frase os símbolos:("!",".","?","..."). str->int"""
    x = frase.count('... ')
    y = frase.count('! ')
    z = frase.count('? ')
    h = frase.count('. ')
    t = frase.count('.')
    s = frase.count('!')
    d = frase.count('?')
    f = frase.count('...')
    return x+y+z+h+t+s+d+f