def contapontuacao(frase):
    '''conta quantas frases existem dentro da string
    str->int'''
    a = str.count(frase,'!')
    b = str.count(frase,'.')
    c = str.count(frase,'?')
    d = frase.count('...')
    d =(d)-2
    
    return a+b+c-d