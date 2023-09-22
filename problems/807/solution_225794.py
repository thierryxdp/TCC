def conta_frases(frase):
    '''Esta e a funcao que conta o numero de frases que
    aparecem em um texto de entrada
    str -> int'''
    f1=frase.count('. ')
    f2=frase.count('!')
    f3=frase.count('?')
    f4=frase.count('...')
    f5=frase.count('.')
    f6=frase.count(' .')
    total=f1+f2+f3+f4+f5+f6
    return total