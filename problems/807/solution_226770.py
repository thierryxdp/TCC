def conta_frases(x):
    '''Esta função conta o número de frases em uma string dado os elementos '.', '!', '?' e '...' divisores de frase.
str-->int'''
    frases=0
    if '...' in x:
        frases=+frases+str.count(x,'...')
    if '.' in x:
        frases=+frases+str.count(x,'.')-3*str.count(x,'...')
    if '?' in x:
        frases=+frases+str.count(x,'?')
    if '!' in x:
        frases=+frases+str.count(x,'!')
 

    return frases