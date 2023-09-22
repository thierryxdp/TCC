def conta_frases(frase):
    '''Esta e a funcao que conta o numero de frases que
    aparecem em um texto de entrada
    str -> int'''
    f1=frase.count(' .')
    f2=frase.count('!')
    f3=frase.count('?')
    f4=frase.count('...')
    for n in f1 and f2 and f3 and f4:
        if f1>=n and f2>=n and f3>=n and f4>=n:
            return n