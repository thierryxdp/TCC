def conta_frases(frase):
    '''Esta e a funcao que conta o numero de frases que
    aparecem em um texto de entrada
    str -> int'''
    f1=frase.count('. ')
    f2=frase.count('!')
    f3=frase.count('?')
    f4=frase.count('.')
    total=f1+f2+f3+f4
    if f1==1 and f2==1 and f3==1 and f4==1:
        return total
    elif f1>1 and f2>1 and f3>1 and f4>1:
        return total