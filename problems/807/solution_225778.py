def conta_frases(frase):
    '''Esta e a funcao que conta o numero de frases que
    aparecem em um texto de entrada
    str -> int'''
    f1='.'
    f2='!'
    f3='?'
    f4='.'
    if f1 and f2 and f3 and f4 in frase:
        return 4
    elif f1 and f2 and f3 in frase:
        return 3
    elif f1 and f4 in frase:
        return 2
    elif f1 and f3 in frase:
        return 2
    elif f1 and f2 in frase:
        return 2
    elif f2 and f3 in frase:
        return 2
    elif f2 and f4 in frase:
        return 2
    elif f3 and f4 in frase:
        return 2
    elif f1 in frase:
        return 1
    elif f2 in frase:
        return 1
    elif f3 in frase:
        return 1
    elif f4 in frase:
        return 1