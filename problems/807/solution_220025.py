def conta_frases (frase):
    ex=frase.split('!')
    inte=frase.split('?')
    pon=frase.split('.')
    dois=frase.split('...')
    return len(ex+inte+pon+dois)