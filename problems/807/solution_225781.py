#a função conta o número de frases que aparecem no texto.
#str->int
def conta_frases(frase):
    a=frase.count('.')
    b=frase.count('!')
    c=frase.count('?')
    d=frase.count('...')
    e=a+b+c+d
    return(e)