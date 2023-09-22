def conta_frases(frase):
    '''Dado uma string frase, retorne o número de frases; string -> int'''
    frase=list(frase)
    list.append(' ')
    a=str.count(frase,'. ')
    b=str.count(frase,'!')
    c=str.count(frase,'?')
    d=str.count(frase,'...')
    return a+b+c+d